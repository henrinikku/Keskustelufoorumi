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

@app.route("/")
def index():
    return "Index"


if __name__ == "__main__":
    app.run()
