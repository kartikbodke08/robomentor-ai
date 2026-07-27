from google import genai
from fastapi import HTTPException, status
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL

from app.prompts.robotics_prompt import build_robotics_prompt
from app.core.logger import logger

from sqlalchemy.orm import Session
from app.services.conversation_service import conversation_service

class AIService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)


    def generate_response(self, db:Session, conversation_id:int, question:str, level:str):

        if not question.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty."
        )


        conversation = conversation_service.get_conversation(
            db = db,
            conversation_id=conversation_id
        )

        if conversation is None :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail = "Conversation not found"
            )

        conversation_service.add_message(
            db = db,
            conversation_id = conversation_id,
            role = "user",
            content = question
        )

        history = conversation_service.get_messages(db = db, conversation_id = conversation_id)

        prompt = build_robotics_prompt(
            question=question,
            level=level,
            history=history
        )
        try:
            
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            
            logger.info(f"Gemini Response generated successfully")

        except Exception as e:
            logger.exception(f"Gemini API Error : {e}")

            raise HTTPException(
                status_code=500,
                detail="Unable to generate AI response, Please try again later"
            )
        
        answer = response.text if response.text else "No reponse generated"

        conversation_service.add_message(
            db = db,
            conversation_id=conversation_id,
            role = "assistant",
            content=answer
        )

        return {
            "question": question,
            "level": level,
            "answer": answer
        }


    def generate_stream_response(
            self,
            db : Session,
            conversation_id: int,
            question: str,
            level: str,
    ):
        if not question.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty."
        )


        conversation = conversation_service.get_conversation(
                    db = db,
                    conversation_id=conversation_id
                )
        
        if conversation is None :
            raise HTTPException(
                status_code=404,
                detail = "Conversation not found"
            )

        conversation_service.add_message(
            db = db,
            conversation_id = conversation_id,
            role = "user",
            content = question
        )

        history = conversation_service.get_messages(db = db, conversation_id = conversation_id)

        prompt = build_robotics_prompt(
            question=question,
            level=level,
            history=history
        )

        try :

            response = self.client.models.generate_content_stream(
                model=GEMINI_MODEL,
                contents = prompt,
            )

        except Exception as e:
            logger.exception(f"Gemini API Error : {e}")

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "Unable to generate AI response, Please try again later"
            )

        answer = ""

        for chunk in response:
            if chunk.text:
                answer += chunk.text
                yield chunk.text

        conversation_service.add_message(
            db = db,
            conversation_id=conversation_id,
            role = "assistant",
            content = answer,
        )


            
ai_service = AIService()