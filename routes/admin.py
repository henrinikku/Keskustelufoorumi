from flask import Blueprint, render_template

from permissions import is_admin

admin = Blueprint("admin", __name__)


@admin.route("/")
@is_admin
def index():
    return render_template("admin.html")
