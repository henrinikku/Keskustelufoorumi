from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from application.forms.auth import RegisterForm, LoginForm
from application.queries.user import add_user, by_username

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET"])
def register():
    return render_template("register.html", form=RegisterForm())


@auth.route("/register", methods=["POST"])
def register_post():
    form = RegisterForm(request.form)

    if not form.validate_and_flash_errors():
        return redirect(url_for("auth.register"))

    existing_user = by_username(form.username.data)

    if existing_user:
        flash("Username is taken")
        return redirect(url_for("auth.register"))

    add_user(username=form.username.data, password=form.password.data)

    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html", form=LoginForm())


@auth.route("/login", methods=["POST"])
def login_post():
    form = LoginForm(request.form)

    if not form.validate_and_flash_errors():
        return redirect(url_for("auth.login"))

    user = by_username(form.username.data)

    if not user or not check_password_hash(user.password, form.password.data):
        flash("Incorrect credentials")
        return redirect(url_for("auth.login"))

    login_user(user)
    return redirect(url_for("root.index"))


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
