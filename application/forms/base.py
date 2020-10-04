from flask import flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, SelectField,
    TextAreaField,
)

from application.queries.generic import add_or_update


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

    def validate_and_flash_errors(self, extra_validators=None):
        result = self.validate(extra_validators)
        if not result:
            self.flash_errors()

        return result

    def save(self, obj):
        self.populate_obj(obj)
        add_or_update(obj)


class StyledSelectField(SelectField):
    def __init__(self, *args, **kwargs):
        """This acts as a placeholder for now"""

        super(StyledSelectField, self).__init__(*args, **kwargs)


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


class StyledTextAreaField(TextAreaField):
    def __init__(self, *args, **kwargs):
        label = kwargs.get("label") or args[0] or ""
        render_kw = kwargs.pop("render_kw", {})
        attributes = {
            **render_kw,
            "class": "textarea",
            "placeholder": label,
        }
        super(StyledTextAreaField, self).__init__(
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
            "class": "button is-block is-link is-fullwidth",
        }
        super(StyledSubmitField, self).__init__(
            render_kw=attributes, *args, **kwargs
        )
