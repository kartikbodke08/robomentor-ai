from google import genai
from fastapi import HTTPException
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL


class AIService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def build_prompt(self, question:str , level:str , history:list)->str:

        history_text = "\n".join(
            f"{msg.role}: {msg.content}"
            for msg in history
        )

        return f"""You are RoboMentor AI.

        You are an expert robotics mentor helping students learn robotics, Arduino, electronics, IoT, sensors, and programming.

        Student Level:
        {level}

        Previous Conversation:
        {history_text}

        Current Question:
        {question}

        Instructions:

        - Answer according to the student's level.
        - Use simple language.
        - Explain step by step.
        - Give real-world examples whenever possible.
        - Encourage curiosity.
        - If code is needed, explain every important line.
        - Use bullet points where appropriate.
        - If the student asks a follow-up question, use the conversation history.
        - If you don't know something, honestly say so instead of making up an answer.
        - Keep answers educational and beginner-friendly.
        """

    def generate_response(self, question:str, level:str, history:list):


        prompt = self.build_prompt(
            question,level,history
        )

        try:
            
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
            print(response)
        except Exception as e:
            print(f"Gemini Error : {e}")

            raise HTTPException(
                status_code=500,
                detail="Unable to generate AI response, Please try again later"
            )
        

        return {
            "question": question,
            "level": level,
            "answer": response.text
        }


            
ai_service = AIService()