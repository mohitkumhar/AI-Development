# backend code

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver

from langgraph.graph.message import add_messages

from langchain_ollama import ChatOllama
import sqlite3


llm = ChatOllama(model="llama3.2:3b")


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    
    return {"messages": [response]}



conn = sqlite3.connect(
        database="chatbot.db", 
        check_same_thread=False
    )

# defining checkpointer
checkpointer = SqliteSaver(conn=conn)

# defining stateGraph
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)



def retrieve_all_threads() -> list:
    all_thread = set()

    for item in checkpointer.list(None):
        all_thread.add(item.config['configurable']['thread_id'])

    return list(all_thread)