from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "TODO Login page"


@auth.route("/register")
def register():
    return "TODO Register page"
