from utils_11 import chatbot
import streamlit as st
from langchain_core.messages import HumanMessage

CONFIG = {"configurable": {"thread_id": "thread-1"}}


if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message['role']):
        st.text(message["message"])
    

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}


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