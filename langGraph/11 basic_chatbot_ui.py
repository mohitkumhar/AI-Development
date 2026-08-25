from utils_11 import chatbot
import streamlit as st
from langchain_core.messages import HumanMessage

CONFIG = {"configurable": {"thread_id": "1"}}

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input("Type here...")

if user_input:
    # first add the message to message_history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=CONFIG)
    
    ai_message = response['messages'][-1].content
    
    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    
    with st.chat_message("assistant"):
        st.text(ai_message)
        
        







