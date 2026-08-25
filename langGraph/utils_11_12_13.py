# backend code

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages

from langchain_ollama import ChatOllama



llm = ChatOllama(model="llama3.2:3b")


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    
    return {"messages": [response]}



# defining checkpointer
checkpointer = InMemorySaver()

# defining stateGraph
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
