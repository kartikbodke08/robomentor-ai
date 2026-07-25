from app.core.database import Base, engine

from app.models.conversation import Conversation
from app.models.message import Message

def init_db():
    Base.metadata.create_all(bind=engine)