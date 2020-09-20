from functools import wraps

from flask_login import current_user

from plugins.login_manager import login_manager


def is_admin_user(func):
    """
    Function decorator to ensure that the current user has admin rights
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if current_user.is_admin():
            return func(*args, **kwargs)

        return login_manager.unauthorized()

    return inner


def is_premium_user(func):
    """
    Function decorator to ensure that the current user has (at least) premium users rights
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if current_user.is_premium():
            return func(*args, **kwargs)

        return login_manager.unauthorized()

    return inner


def is_normal_user(func):
    """
    Function decorator to ensure that the current user is logged in
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if current_user.is_normal():
            return func(*args, **kwargs)

        return login_manager.unauthorized()

    return inner
