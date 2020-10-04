from flask import Blueprint, render_template
from flask_login import current_user

from application.decorators.permissions import is_normal_user
from application.queries.category import readable_by_user

root = Blueprint("root", __name__)


@root.route("/")
@is_normal_user
def index():
    categories = readable_by_user(current_user).all()
    return render_template("index.html", communities=categories)
