from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from typing import List


app = FastAPI()
client = Groq(api_key="")

# Data model
class Message(BaseModel):
    content: str

# In-memory database


# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI API!"}


# Add tea

# Chat route - this is the important one
@app.post("/chat")
def chat(message: Message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content}
        ]
    )
    reply = response.choices[0].message.content
    return {"reply": reply}
