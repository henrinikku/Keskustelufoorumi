from wtforms import validators

from application.forms.base import (
    StyledStringField, StyledTextAreaField,
    StyledSubmitField, BaseForm,
)


class ConversationForm(BaseForm):
    title = StyledStringField(
        "Title",
        [validators.DataRequired(), validators.Length(min=3, max=50)]
    )
    message = StyledTextAreaField("Message")
    submit = StyledSubmitField("Start conversation")


class MessageForm(BaseForm):
    message = StyledTextAreaField(
        "Reply with message",
        [validators.DataRequired(), validators.Length(min=3)]
    )
    submit = StyledSubmitField("Send message")


class EditMessageForm(BaseForm):
    message = StyledTextAreaField(
        "Edit message",
        [validators.DataRequired(), validators.Length(min=3)]
    )
    submit = StyledSubmitField("Submit changes")
