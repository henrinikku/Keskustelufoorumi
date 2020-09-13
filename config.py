import os
from abc import ABC
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(ABC):
    DEBUG = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(hours=3)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEVELOPMENT = True
    REMEMBER_COOKIE_DURATION = timedelta(minutes=5)


class ProductionConfig(BaseConfig):
    pass
