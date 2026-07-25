from fastapi import FastAPI, APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_services import ai_service

from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse,
                summary="Ask RoboMentor a robotics related question",
                description="""
                Ask RoboMentor any robotics, Arduino, electronics,
                IoT, sensor, or programming question.

                The response is personalized according to the student's level
                and previous conversation history.
                """,
                tags=["AI Chat"]
             )
def chat(request: ChatRequest) :
    
    return ai_service.generate_response(
        session_id = request.session_id,
        question = request.question,
        level = request.level ,
    )



