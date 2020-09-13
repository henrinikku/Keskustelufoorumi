from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


# TODO Use
class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), length(min=3, max=15)]
    )
    password = PasswordField(
        "Password", validators=[
            DataRequired(), length(min=8),
            EqualTo("confirm", message="Passwords do not match")
        ]
    )
    confirm = PasswordField("Confirm password")
