from wtforms import validators

from application.forms.base import (
    BaseForm, StyledSubmitField, StyledSelectField,
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
