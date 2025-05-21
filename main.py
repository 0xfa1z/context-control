from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import json

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the OpenAI client
client = OpenAI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Log the full conversation
        print("\n=== Full Conversation ===")
        for msg in request.messages:
            print(f"\n{msg.role.upper()}:")
            print(msg.content)
        print("\n======================\n")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": msg.role, "content": msg.content} for msg in request.messages]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)} 