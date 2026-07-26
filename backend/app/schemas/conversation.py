from pydantic import BaseModel
from app.schemas.chat import ChatMessage

from typing import List

class ConversationResponse(BaseModel):

    id: int
    messages: list[ChatMessage]