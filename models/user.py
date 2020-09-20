import enum

from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from plugins.db import db
from . import BaseModel


# Names, not values, are persisted
class UserRole(enum.Enum):
    normal = 1
    premium = 2
    admin = 3


class User(BaseModel, UserMixin):
    __tablename__ = "User"

    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(
        db.Enum(UserRole), nullable=False,
        default=UserRole.normal.name, server_default=UserRole.normal.name,
    )

    def __init__(self, **kwargs):
        password = kwargs.pop("password")
        hashed_password = generate_password_hash(password)
        super(User, self).__init__(password=hashed_password, **kwargs)

    def is_admin(self):
        return self.is_authenticated and self.role == UserRole.admin

    def is_premium(self):
        return self.is_authenticated and self.role in [
            UserRole.admin, UserRole.premium
        ]

    def is_normal(self):
        return self.is_authenticated
