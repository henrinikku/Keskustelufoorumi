from application.db import db
from application.models import Category


def by_id(id):
    return Category.query.get(id)


def by_user(user):
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


def add_or_update(category):
    if not category.id:
        db.session.add(category)

    db.session.commit()

def delete_category(category_id):
    category = by_id(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
