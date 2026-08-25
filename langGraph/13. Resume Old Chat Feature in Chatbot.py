from utils_11 import chatbot
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# utils
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id


def add_thread_in_history(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)
        
def reset_thread_id():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    st.session_state["message_history"] = []
    add_thread_in_history(st.session_state['thread_id'])

def load_conversation(thread_id):
    # print(chatbot.get_state(config={"configurable": {"thread_id": thread_id}}).values)
    return chatbot.get_state(config={"configurable": {"thread_id": thread_id}}).values['messages']




# session setup
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
if 'chat_threads' not in st.session_state:
    st.session_state["chat_threads"] = []
    

add_thread_in_history(st.session_state['thread_id'])

CONFIG = {"configurable": {"thread_id": st.session_state['thread_id']}}

# side bar UI
st.sidebar.title("LangGraph ChatBot")

if st.sidebar.button("New Chat"):
    reset_thread_id()
    

st.sidebar.header("My Conversations")

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        
        temp_messages = []
        
        for message in messages:
            role=''
            if isinstance(message, HumanMessage):
                role = "user"
            elif isinstance(message, AIMessage):
                role = "assistant"
            
            temp_messages.append({"role": role, "message": message.content})
        
        st.session_state["message_history"] = temp_messages
            
        
            

# loading the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message['role']):
        st.text(message["message"])
    

#{'role': 'user', 'content': 'Hi', thread_id: "thread-1"}
#{'role': 'assistant', 'content': 'Hi=ello', thread_id: "thread-2"}


user_input = st.chat_input("Type Here...")

if user_input:
    
    # add user message to message history

    st.session_state["message_history"].append({"role": "user", "message": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    with st.chat_message("assistant"):
        
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            )
        )

    st.session_state["message_history"].append({"role": "assistant", "message": ai_message})