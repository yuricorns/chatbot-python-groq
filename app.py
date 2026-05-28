import streamlit as st
from groq import Groq

client = Groq(api_key="")

st.title("My AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.history
    )
    
    reply = response.choices[0].message.content
    
    st.session_state.history.append({
        "role": "assistant",
        "content": reply
    })
    
    st.rerun()