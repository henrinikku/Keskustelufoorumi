from werkzeug.security import generate_password_hash

from app import db


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

    def __init__(self, **kwargs):
        password = kwargs.pop("password")
        hashed_password = generate_password_hash(password)
        super(User, self).__init__(password=hashed_password, **kwargs)
