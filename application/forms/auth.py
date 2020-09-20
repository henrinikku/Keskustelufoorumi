from wtforms import validators

from application.forms.base import (
    BaseForm, StyledStringField, StyledPasswordField,
    StyledSubmitField,
)


class RegisterForm(BaseForm):
    username = StyledStringField(
        "Username",
        [validators.DataRequired(), validators.Length(min=3, max=20)],
        render_kw={"autofocus": True}
    )
    password = StyledPasswordField("Password", [
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo("confirm_password"),
    ])
    confirm_password = StyledPasswordField("Confirm password")
    submit = StyledSubmitField("Register")


class LoginForm(BaseForm):
    username = StyledStringField(
        "Username",
        [validators.DataRequired(), validators.Length(min=3, max=20)],
        render_kw={"autofocus": True}
    )
    password = StyledPasswordField("Password", [
        validators.DataRequired(),
        validators.Length(min=8),
    ])
    submit = StyledSubmitField("Log In")
