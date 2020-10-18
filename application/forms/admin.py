from wtforms import validators

from application.forms.base import (
    BaseForm, StyledSubmitField, StyledSelectField, StyledStringField,
    StyledQueryMultiSelectField,
)
from application.models import UserRole
from application.queries.user import all_users_except_current


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
    banned_users = StyledQueryMultiSelectField(
        label="Banned users",
        query_factory=all_users_except_current,
        get_pk=lambda user: user.id,
        get_label=lambda user: user.username,
        allow_blank=True,
    )
    submit = StyledSubmitField("Save")
