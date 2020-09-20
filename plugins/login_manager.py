from flask_login import LoginManager
from models import User

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

