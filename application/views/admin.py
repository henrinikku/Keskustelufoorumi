from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user

from application.decorators.permissions import is_admin_user, is_premium_user
from application.queries import user as user_queries

admin = Blueprint("admin", __name__)


@admin.route("/")
@is_premium_user
def index():
    return render_template("admin.html")


@admin.route("/user")
@is_admin_user
def users():
    users = user_queries.all_users_except(current_user.id).all()
    return render_template("admin_users.html", users=users)


@admin.route("/user/<id>/edit")
@is_admin_user
def edit_user(id):
    if id == current_user.id:
        return redirect(url_for("admin.users"))

    user = user_queries.by_id(id)
    return render_template("admin_edit_user.html", user=user)


@admin.route("/user/<id>/delete")
@is_admin_user
def delete_user(id):
    if id != current_user.id:
        user_queries.delete_user(id)

    return redirect(url_for("admin.users"))


@admin.route("/community")
@is_premium_user
def communities():
    return render_template("admin_communities.html")
