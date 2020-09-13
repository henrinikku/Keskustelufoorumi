from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from db import db
from . import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = "User"

    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(self, **kwargs):
        password = kwargs.pop("password")
        hashed_password = generate_password_hash(password)
        super(User, self).__init__(password=hashed_password, **kwargs)
