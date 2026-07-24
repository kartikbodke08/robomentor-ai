from pydantic import BaseModel, Field
from enum import Enum


class StudentLevel(str,Enum):
    beginner = "Beginner"
    intermediate = "Intermediate"
    advanced = "Advanced"

class ChatMessage(BaseModel):
    role: str = Field(...,example=["user"],description="Role of the message sender")
    content: str = Field(...,examples=["What is PWM"], description="Content of the conversation message")

class ChatRequest(BaseModel):
    session_id:str = Field(...,description="Unique conversation session ID")
    question: str = Field(...,min_length=3,max_length=1000, description = "Student's robotics question", examples=["What is PWM in Arduino?"])
    level: StudentLevel
    history: list[ChatMessage] = Field(default_factory=list, description="Previous conversation history")


class ChatResponse(BaseModel) :
    question: str  = Field(description="Student's original question")
    level: StudentLevel = Field(description="Student's learning level")
    answer: str = Field(description="AI generated response")
