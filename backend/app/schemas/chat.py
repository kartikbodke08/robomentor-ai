from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    question: str
    level: str
    history: list[ChatMessage] = Field(default_factory=list)