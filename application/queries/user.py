from sqlalchemy import not_

from application.db import db
from application.models import User


def all_users_except(user_id):
    return User.query.filter(not_(User.id == user_id)).order_by(User.username)

def by_id(user_id):
    return User.query.get(user_id)

def by_username(username):
    return User.query.filter_by(username=username).first()


def add_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    user = by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
