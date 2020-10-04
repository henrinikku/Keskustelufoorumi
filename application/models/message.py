from application.db import db
from . import BaseModel


class Message(BaseModel):
    __tablename__ = "Message"

    message = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship("User", back_populates="messages")

    conversation_id = db.Column(db.Integer, db.ForeignKey("Conversation.id"))
    conversation = db.relationship("Conversation", back_populates="messages")

    def __str__(self):
        datetime = self.created.strftime('%d.%m.%Y %H:%M:%S')
        return f"By {self.user.username} at {datetime}"
