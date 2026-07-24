from google import genai
from fastapi import HTTPException
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL

from prompts.robotics_prompt import build_robotics_prompt
from app.core.logger import logger

class AIService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)


    def generate_response(self, question:str, level:str, history:list):


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

            
            logger.info(f"Gemini Response: {response.text}")

        except Exception:
            logger.exception("Gemini API Error")

            raise HTTPException(
                status_code=500,
                detail="Unable to generate AI response, Please try again later"
            )
        
        answer = response.text if response.text else "No reponse generated"

        return {
            "question": question,
            "level": level,
            "answer": answer
        }


            
ai_service = AIService()