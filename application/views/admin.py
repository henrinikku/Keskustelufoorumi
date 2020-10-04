from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from application.db import db
from application.decorators.permissions import is_admin_user, is_premium_user
from application.forms.admin import UserForm, CategoryForm
from application.models import Category
from application.queries import user as user_queries
from application.queries.generic import add_or_update
from application.queries.category import (
    editable_by_user, by_id, delete_category, by_name,
)

admin = Blueprint("admin", __name__)


@admin.route("/")
@is_premium_user
def index():
    return render_template("admin.html")


@admin.route("/user")
@is_admin_user
def users():
    users = user_queries.all_users_except(current_user.id).all()

    return render_template(
        "admin_users.html", title="Manage users", users=users
    )


@admin.route("/user/<id>/edit", methods=["GET", "POST"])
@is_admin_user
def edit_user(id):
    if id == current_user.id:
        return redirect(url_for("admin.users"))

    user = user_queries.by_id(id)
    form = UserForm(obj=user)

    if request.method == "POST" and form.validate():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("admin.users"))

    return render_template(
        "admin_edit_user.html",
        title=f"Edit user {user.username}",
        id=id,
        form=form
    )


@admin.route("/user/<id>/delete")
@is_admin_user
def delete_user(id):
    if id != current_user.id:
        user_queries.delete_user(id)

    return redirect(url_for("admin.users"))


@admin.route("/community")
@is_premium_user
def communities():
    categories = editable_by_user(current_user).all()

    return render_template(
        "admin_communities.html",
        title="Manage communities",
        communities=categories
    )


@admin.route("/community/<id>/edit", methods=["GET", "POST"])
@is_premium_user
def edit_community(id):
    category = by_id(id) or Category()
    form = CategoryForm(obj=category)

    if request.method == "POST" and form.validate_and_flash_errors():
        existing_category = by_name(form.name.data)
        if existing_category and existing_category.id != int(id):
            flash("Community name is taken")
        else:
            category.user_id = category.user_id or current_user.id
            form.save(category)
            return redirect(url_for("admin.communities"))

    title = f"Edit community {category.name}" if category.name else "Add community"

    return render_template(
        "admin_edit_community.html", title=title, id=id, form=form
    )


@admin.route("/community/<id>/delete")
@is_premium_user
def delete_community(id):
    delete_category(id)
    return redirect(url_for("admin.communities"))
