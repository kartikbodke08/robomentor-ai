from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message

class ConversationService :

    def create_conversation(self, db: Session) :

        conversation = Conversation()

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def get_conversation(self, db:Session, conversation_id:int) :

        return(
            db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

    def save_message(self, db:Session, conversation_id:int, role: str, content: str):
        message = Message(conversation_id =conversation_id,
                          role = role,
                          content = content)

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    def get_message(self, db:Session, conversation_id:int):

        return (db.query(Message)
                .filter(Message.conversation_id == conversation_id)
                .order_by(Message.id)
                .all()
                )
        

    

conversation_service = ConversationService()