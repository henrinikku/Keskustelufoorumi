from wtforms import validators

from application.forms.base import (
    StyledStringField, StyledSubmitField, BaseForm,
)


class SearchForm(BaseForm):
    keyword = StyledStringField(
        "Keyword",
        [validators.DataRequired(), validators.Length(min=3, max=50)]
    )
    submit = StyledSubmitField("Search")
