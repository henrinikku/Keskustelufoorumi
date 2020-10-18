from application.db import db
from . import BaseModel

BannedUser = db.Table(
    "BannedUser",
    db.Model.metadata,
    db.Column(
        "user_id", db.Integer,
        db.ForeignKey("User.id"), primary_key=True
    ),
    db.Column(
        "category_id", db.Integer,
        db.ForeignKey("Category.id"), primary_key=True
    )
)


class Category(BaseModel):
    __tablename__ = "Category"

    name = db.Column(db.String(), unique=True, nullable=False)
    conversations = db.relationship(
        "Conversation", back_populates="category", lazy=True
    )
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship("User", back_populates="categories")
    banned_users = db.relationship(
        "User", secondary=BannedUser, backref="Category"
    )
