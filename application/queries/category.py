from flask_login import current_user
from sqlalchemy import not_
from sqlalchemy.orm import joinedload

from application.db import db
from application.models import Category, Conversation, User


def by_id(id):
    return (
        Category
            .query
            .filter(not_(Category.banned_users.any(User.id == current_user.id)))
            .filter(Category.id == id)
            .first()
    )


def user_is_banned_from(user_id, category_id):
    return (
        Category
            .query
            .filter(Category.banned_users.any(User.id == user_id))
            .filter(Category.id == category_id)
            .first()
    )


def by_id_with_conversations(id):
    joins = joinedload(Category.conversations).joinedload(Conversation.messages)
    return (
        Category
            .query
            .options(joins)
            .filter(not_(Category.banned_users.any(User.id == current_user.id)))
            .filter(Category.id == id)
            .first()
    )


def by_name(name):
    return (
        Category
            .query
            .filter(not_(Category.banned_users.any(User.id == current_user.id)))
            .filter(Category.name == name)
            .first()
    )


def readable_by_user(user):
    if user.is_admin():
        return Category.query.order_by(Category.name)

    return (
        Category
            .query
            .filter(not_(Category.banned_users.any(User.id == current_user.id)))
            .order_by(Category.name)
    )


def editable_by_user(user):
    """Categories the given user is permitted to edit"""

    if user.is_admin():
        return Category.query.order_by(Category.name)

    if user.is_premium():
        return (
            Category
                .query
                .filter(Category.user_id == user.id)
                .order_by(Category.name)
        )

    return []


def delete_category(category_id):
    category = by_id(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
