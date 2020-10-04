from sqlalchemy.orm import joinedload

from application.db import db
from application.models import Category, Conversation


def by_id(id):
    return Category.query.get(id)


def by_id_with_conversations(id):
    joins = joinedload(Category.conversations).joinedload(Conversation.messages)
    return Category.query.options(joins).get(id)


def by_name(name):
    return Category.query.filter(Category.name == name).first()


def readable_by_user(user):
    if user.is_admin():
        return Category.query.order_by(Category.name)

    # TODO admins can ban users from viewing categories
    return Category.query.order_by(Category.name)


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
