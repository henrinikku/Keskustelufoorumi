from sqlalchemy.orm import joinedload

from application.db import db
from application.models import Conversation, Message


def by_id(id):
    return Conversation.query.get(id)


def by_id_with_messages_and_users(id):
    return (
        Conversation
            .query
            .options(joinedload(Conversation.user))
            .options(joinedload(Conversation.messages).joinedload(Message.user))
            .get(id)
    )


def delete_conversation(id):
    conversation = by_id(id)
    if conversation:
        db.session.delete(conversation)
        db.session.commit()