from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import check_password_hash

from app import db
from models import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@auth.route("/register", methods=["POST"])
def register_post():
    # TODO Use Flask-WTF https://flask-wtf.readthedocs.io/en/latest/
    username = request.form.get("username")
    password = request.form.get("password")
    password_again = request.form.get("password_again")

    if not username or not password or password != password_again:
        flash("username is invalid or passwords do not match")
        return redirect(url_for("auth.register"))

    old_user = User.query.filter_by(username=username).first()
    if old_user:
        flash("username is taken")
        return redirect(url_for("auth.register"))

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

    # TODO Session management
    return redirect(url_for("root.index"))


@auth.route("/logout")
def logout():
    return "Logout"
