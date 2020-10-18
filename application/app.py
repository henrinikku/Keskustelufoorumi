import os

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

from application.csrf import csrf
from application.db import db
from application.login_manager import login_manager
from application.views import root, auth, admin, community

load_dotenv()

app = Flask(__name__)

# Load configuration
config = import_string(os.environ.get("APP_SETTINGS"))
app.config.from_object(config())

# Register db
db.init_app(app)

# Register login manager
login_manager.init_app(app)

# Enable CSRF protection
csrf.init_app(app)

# Register routes
app.register_blueprint(root)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(community, url_prefix="/community")
