from pydantic import BaseModel

class ChatResponse(BaseModel) :
    question: str
    level: str
    answer: str