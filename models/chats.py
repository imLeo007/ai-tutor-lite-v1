from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship

from database import Base

class Chat(Base):

    __tablename__ = "chats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    prompt = Column(
        String,
        nullable=False
    )

    response = Column(
        String,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="history"
    )