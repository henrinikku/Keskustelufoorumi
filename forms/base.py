from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class BaseForm(FlaskForm):
    class Meta:
        csrf = False

    def _format_errors(self):
        if not self.errors:
            return

        for field, errors in self.errors.items():
            label = getattr(self, field).label.text
            for error in errors:
                yield f"{label}: {error}"

    def flash_errors(self):
        for error in self._format_errors():
            flash(error)


class StyledStringField(StringField):
    def __init__(self, *args, **kwargs):
        label = kwargs.get("label") or args[0] or ""
        render_kw = kwargs.pop("render_kw", {})
        attributes = {
            **render_kw,
            "class": "input",
            "type": "text",
            "placeholder": label,
        }
        super(StyledStringField, self).__init__(
            render_kw=attributes, *args, **kwargs
        )


class StyledPasswordField(PasswordField):
    def __init__(self, *args, **kwargs):
        label = kwargs.get("label") or args[0] or ""
        render_kw = kwargs.pop("render_kw", {})
        attributes = {
            **render_kw,
            "class": "input",
            "type": "password",
            "placeholder": label,
        }
        super(StyledPasswordField, self).__init__(
            render_kw=attributes, *args, **kwargs
        )


class StyledSubmitField(SubmitField):
    def __init__(self, *args, **kwargs):
        render_kw = kwargs.pop("render_kw", {})
        attributes = {
            **render_kw,
            "class": "button is-block is-info is-fullwidth",
        }
        super(StyledSubmitField, self).__init__(
            render_kw=attributes, *args, **kwargs
        )
