from fastapi import FastAPI
from app.routes import chat

app = FastAPI(title="AI-Assistant")

app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "AI Assistant is running"}
