from application.db import db


def add_or_update(obj):
    if not obj.id:
        db.session.add(obj)

    db.session.commit()
