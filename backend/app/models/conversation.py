from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base

class Conversation(Base) :

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index = True)

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )