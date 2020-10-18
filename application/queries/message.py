from sqlalchemy.orm import joinedload

from application.db import db
from application.models import Message


def by_id(id):
    return Message.query.get(id)


def by_id_with_conversation(id):
    return Message.query.options(joinedload(Message.conversation)).get(id)


def delete_message(id):
    message = by_id(id)
    if message:
        db.session.delete(message)
        db.session.commit()
