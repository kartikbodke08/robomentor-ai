from fastapi import HTTPException, status

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.conversation_service import conversation_service

from app.schemas.conversation import ConversationResponse
from app.schemas.chat import ChatMessage

router = APIRouter()

@router.post("/conversation")
def create_conversation(db:Session = Depends(get_db)) :

    conversation = conversation_service.create_conversation(db)

    return {
        "conversation_id" : conversation.id
    }

@router.get(
        "/conversation/{conversation_id}",
        response_model=ConversationResponse,
        summary="Get conversation history",
        description="Returns all messages belonging to a conversation.",
        tags=["Conversation"]
        )
def get_messages(conversation_id : int, db: Session = Depends(get_db)) :

    conversation = conversation_service.get_conversation(
        db=db,
        conversation_id=conversation_id,
    )


    if conversation is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Conversation not found"
        )

    messages = conversation_service.get_messages(
        db = db,
        conversation_id=conversation_id
    )

    chat_messages = [
        ChatMessage(
            role = message.role,
            content = message.content,
        )
        for message in messages
    ]


    return ConversationResponse(
        id = conversation.id,
        messages = chat_messages
    )



    

