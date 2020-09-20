from flask import Blueprint, render_template

from decorators.permissions import is_admin_user

admin = Blueprint("admin", __name__)


@admin.route("/")
@is_admin_user
def index():
    return render_template("admin.html")
