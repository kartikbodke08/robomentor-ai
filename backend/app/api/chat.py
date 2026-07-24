from fastapi import FastAPI, APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_services import ai_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) :
    
    return ai_service.generate_response(
        question = request.question,
        level = request.level ,
        history = request.history
    )



