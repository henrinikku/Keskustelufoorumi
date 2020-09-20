from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from forms.auth import RegisterForm, LoginForm
from models import User
from plugins.db import db

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET"])
def register():
    return render_template("register.html", form=RegisterForm())


@auth.route("/register", methods=["POST"])
def register_post():
    form = RegisterForm(request.form)

    if not form.validate():
        form.flash_errors()
        return redirect(url_for("auth.register"))

    existing_user = User.query.filter_by(username=form.username.data).first()
    if existing_user:
        flash("Username is taken")
        return redirect(url_for("auth.register"))

    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html", form=LoginForm())


@auth.route("/login", methods=["POST"])
def login_post():
    form = LoginForm(request.form)

    if not form.validate():
        form.flash_errors()
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(username=form.username.data).first()
    if not user or not check_password_hash(user.password, form.password.data):
        flash("Incorrect credentials")
        return redirect(url_for("auth.login"))

    login_user(user)
    return redirect(url_for("root.index"))


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
