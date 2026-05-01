from fastapi import APIRouter
from models.common import ChatRequest, ChatResponse
from services.chat_service import process_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_endpoint(request: ChatRequest):
    response = await process_chat(request.message)
    return ChatResponse(response=response)

