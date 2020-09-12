from app import db
from flask_sqlalchemy import SQLAlchemy


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.now())
    updated = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )


class User(BaseModel):
    __tablename__ = "User"
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
