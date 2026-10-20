
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Day 9 Learning API",
    description="My first API built with FastAPI",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/search")
def search(q: str):
    return {"search_query": q}


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "question": request.question,
        "answer": f"You asked: {request.question}",
    }
