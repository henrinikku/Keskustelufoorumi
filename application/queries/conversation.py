from flask_login import current_user
from sqlalchemy import not_
from sqlalchemy.orm import joinedload

from application.db import db
from application.models import Conversation, Message, Category, User


def search_by_keyword(keyword):
    title = f"%{keyword}%"
    return (
        Conversation
            .query
            .filter(not_(Conversation.category.has(
            Category.banned_users.any(User.id == current_user.id))))
            .filter(Conversation.title.like(title))
            .order_by(Conversation.created.desc())
    )


def by_id(id):
    return Conversation.query.get(id)


def by_id_with_messages_and_users(id):
    return (
        Conversation
            .query
            .options(joinedload(Conversation.user))
            .options(joinedload(Conversation.messages).joinedload(Message.user))
            .filter(not_(Conversation.category.has(
            Category.banned_users.any(User.id == current_user.id))))
            .filter(Conversation.id == id)
            .first()
    )


def delete_conversation(id):
    conversation = by_id(id)
    if conversation:
        db.session.delete(conversation)
        db.session.commit()
