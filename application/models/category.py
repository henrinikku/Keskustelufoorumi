from application.db import db
from . import BaseModel


class Category(BaseModel):
    __tablename__ = "Category"

    name = db.Column(db.String(), unique=True, nullable=False)
    conversations = db.relationship(
        "Conversation", back_populates="category", lazy=True
    )

    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship("User", back_populates="categories")
