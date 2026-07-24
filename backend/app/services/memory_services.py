class MemoryService:

    def __init__(self):
        self.memory = {}

    def get_history(self, session_id:str) :

        if session_id not in self.memory :
            self.memory[session_id] = []
        return self.memory[session_id]

    def add_message(self, session_id:str, role:str, content:str) :

        history = self.get_history(session_id)

        history.append({
            "role":role,
            "content":content
        })

memory_service = MemoryService()
