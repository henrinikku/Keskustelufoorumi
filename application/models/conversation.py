from application.db import db
from . import BaseModel


class Conversation(BaseModel):
    __tablename__ = "Conversation"

    title = db.Column(db.String(), nullable=False)
    message = db.Column(db.String())
    messages = db.relationship(
        "Message", back_populates="conversation",
        lazy=True, order_by="Message.created.desc()"
    )

    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship("User", back_populates="conversations")

    category_id = db.Column(db.Integer, db.ForeignKey("Category.id"))
    category = db.relationship("Category", back_populates="conversations")
