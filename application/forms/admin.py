from wtforms import validators

from application.forms.base import (
    BaseForm, StyledSubmitField, StyledSelectField, StyledStringField,
)
from application.models import UserRole


class UserForm(BaseForm):
    role = StyledSelectField(
        "Role",
        [validators.DataRequired()],
        choices=UserRole.choices(),
        coerce=UserRole.coerce,
    )
    submit = StyledSubmitField("Save")


class CategoryForm(BaseForm):
    name = StyledStringField(
        "Name",
        [validators.DataRequired(), validators.Length(min=3, max=28)]
    )
    submit = StyledSubmitField("Save")
