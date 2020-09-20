from flask import Blueprint, render_template
from decorators.permissions import is_normal_user

root = Blueprint("root", __name__)


@root.route("/")
@is_normal_user
def index():
    return render_template("index.html")
