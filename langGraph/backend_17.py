# backend code

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver

from langgraph.graph.message import add_messages

from langchain_ollama import ChatOllama
import sqlite3

from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("STOCK_API_KEY")

llm = ChatOllama(model="llama3.2:3b", temperature=0)

# tools
search_tool = DuckDuckGoSearchRun(region="us-en")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """

    try:
        if operation in ["add", "+"]:
            result = first_num + second_num
        elif operation in ["sub", "-"]:
            result = first_num - second_num
        elif operation in ["mul", "*"]:
            result = first_num * second_num
        elif operation in ["div", "/"]:
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}

        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}

    except Exception as e:
        return {"error": str(e)}
    

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g., 'AAPL', 'TSLA')
    using Alpha Vantage with API key in the URL
    """

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    r = requests.get(url)

    return r.json()


# make the list of tool
tools = [search_tool, calculator, get_stock_price]

# Make the LLM tool-aware
llm_with_tools = llm.bind_tools(tools)

#state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    
# graph nodes
def chat_node(state: ChatState):
    """LLM node may answer or request a tool call"""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools) # executes the tool calls


conn = sqlite3.connect(
        database="chatbot.db", 
        check_same_thread=False
    )

# defining checkpointer
checkpointer = SqliteSaver(conn=conn)

# defining stateGraph
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)

graph.add_edge("tools", "chat_node")


chatbot = graph.compile(checkpointer=checkpointer)


def retrieve_all_threads() -> list:
    all_thread = set()

    for item in checkpointer.list(None):
        all_thread.add(item.config['configurable']['thread_id'])

    return list(all_thread)