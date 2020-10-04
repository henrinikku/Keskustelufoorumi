from application.db import db
from application.models import Message


def by_id(id):
    return Message.query.get(id)


def delete_message(id):
    message = by_id(id)
    if message:
        db.session.delete(message)
        db.session.commit()
