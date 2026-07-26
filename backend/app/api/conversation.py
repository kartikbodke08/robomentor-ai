from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.conversation_service import conversation_service

router = APIRouter()

@router.post("/conversation")
def create_conversation(db:Session = Depends(get_db)) :

    conversation = conversation_service.create_conversation(db)

    return {
        "conversation_id" : conversation.id
    }