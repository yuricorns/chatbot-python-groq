# chatbot-python-groq

# AI Chatbot — Python + Groq LLM

A conversational AI chatbot built in pure Python using the Groq LLM API.
Features a clean chat UI built with Streamlit and persistent conversation
memory across the session.

## Features
- Real-time AI responses using Groq LLM (llama-3.3-70b-versatile)
- Conversation memory — remembers everything said in the session
- Clean chat UI with Streamlit
- Custom AI personality via system prompt

## Tech Stack
- Python
- Groq SDK
- Streamlit
- llama-3.3-70b-versatile model

## How to Run

1. Clone the repo
   git clone https://github.com/yuricorns/chatbot-python-groq

2. Install dependencies
   pip install groq streamlit

3. Add your Groq API key in app.py

4. Run the app
   python -m streamlit run app.py

## What I learned building this
- Direct LLM API calls in pure Python without automation tools
- Managing conversation history manually as a messages list
- Building and serving an AI app with a real UI using Streamlit
