import os

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

from db import db
from login_manager import login_manager
from routes import root, auth, admin

load_dotenv()

app = Flask(__name__)

# Load configuration
config = import_string(os.environ.get("APP_SETTINGS"))
app.config.from_object(config())

# Register db
db.init_app(app)

# Register login manager
login_manager.init_app(app)

# Register routes
app.register_blueprint(root)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(admin, url_prefix="/admin")

if __name__ == "__main__":
    app.run()
