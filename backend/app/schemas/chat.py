from pydantic import BaseModel, Field
from enum import Enum


class StudentLevel(str,Enum):
    beginner = "Beginner"
    intermediate = "Intermediate"
    advanced = "Advanced"

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    question: str = Field(...,min_length=3,max_length=1000, description = "Student's robotics question")
    level: StudentLevel
    history: list[ChatMessage] = Field(default_factory=list)


class ChatResponse(BaseModel) :
    question: str 
    level: StudentLevel
    answer: str
