from functools import wraps

from flask_login import current_user
from werkzeug.exceptions import Forbidden


def is_admin(func):
    """
    Function decorator to ensure that the current user has admin rights
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            raise Forbidden("Forbidden")
        return func(*args, **kwargs)

    return inner


def is_premium(func):
    """
    Function decorator to ensure that the current user has (at least) premium users rights
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_premium():
            raise Forbidden("Forbidden")
        return func(*args, **kwargs)

    return inner
