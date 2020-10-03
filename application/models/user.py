import enum

from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from application.db import db
from . import BaseModel


# Names, not values, are persisted
class UserRole(enum.Enum):
    normal = 1
    premium = 2
    admin = 3

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(field.name, field.name.capitalize()) for field in cls]

    @classmethod
    def coerce(cls, obj):
        return obj if isinstance(obj, UserRole) else UserRole[obj]


class User(BaseModel, UserMixin):
    __tablename__ = "User"

    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(
        db.Enum(UserRole), nullable=False,
        default=UserRole.normal.name, server_default=UserRole.normal.name,
    )
    categories = db.relationship("Category", back_populates="user", lazy=True)
    conversations = db.relationship(
        "Conversation", back_populates="user", lazy=True
    )
    messages = db.relationship("Message", back_populates="user", lazy=True)

    def __init__(self, **kwargs):
        password = kwargs.pop("password")
        hashed_password = generate_password_hash(password)
        super(User, self).__init__(password=hashed_password, **kwargs)

    def is_admin(self):
        return self.role == UserRole.admin

    def is_premium(self):
        return self.role in [UserRole.admin, UserRole.premium]
