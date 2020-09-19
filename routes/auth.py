from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from db import db
from models import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@auth.route("/register", methods=["POST"])
def register_post():
    username = request.form.get("username")
    password = request.form.get("password")
    password_again = request.form.get("password_again")

    register_url = url_for("auth.register")

    if not username or len(username) < 3:
        flash("Username is invalid")
        return redirect(register_url)

    old_user = User.query.filter_by(username=username).first()
    if old_user:
        flash("Username is taken")
        return redirect(register_url)

    if not password or len(password) < 8:
        flash("Password is invalid")
        return redirect(register_url)

    if not password == password_again:
        flash("Passwords do not match")
        return redirect(register_url)

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect credentials")
        return redirect(url_for("auth.login"))

    login_user(user)
    return redirect(url_for("root.index"))


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
