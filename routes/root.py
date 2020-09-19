from flask import Blueprint, render_template
from flask_login import login_required

root = Blueprint("root", __name__)


@root.route("/")
@login_required
def index():
    return render_template("index.html")
