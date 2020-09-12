import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

load_dotenv()

app = Flask(__name__)

config = import_string(os.environ.get("APP_SETTINGS"))
app.config.from_object(config())

db = SQLAlchemy(app)

# TODO Fix this?
from routes import *

app.register_blueprint(root)
app.register_blueprint(auth, url_prefix="/auth")

if __name__ == "__main__":
    app.run()
