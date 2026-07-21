class AIService:

    def generate_response(self, question:str, level:str):

        return {
            "question": question,
            "level": level,
            "answer": f"This is a dummy reponse for '{question}'."
        }
ai_service = AIService()