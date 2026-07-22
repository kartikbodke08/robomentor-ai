from google import genai

from app.core.config import GEMINI_API_KEY, GEMINI_MODEL


class AIService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, question:str, level:str):

        prompt = f"""
        You are RoboMentor AI.

        The student level is:
        {level}

        Answer the following robotics question clearly.

        Question:
        {question}
        """

        try:
            
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
            print(response)
        except Exception as e:
            import traceback

            print(type(e))
            print(e)
            traceback.print_exc()
            raise

        return {
            "question": question,
            "level": level,
            "answer": response.text
        }

    
ai_service = AIService()