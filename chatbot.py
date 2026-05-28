import streamlit as st
from groq import Groq

client = Groq(api_key="")
history = []

while True:
    # Step 5 - get user input
    user_input = input("You: ")
    
    # Step 6 - add to history
    history.append({"role": "user", "content": user_input})
    
    # Step 7 - send to API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
    
    # Step 8 - print response
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    print("Bot:", reply)