from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user

from application.forms.conversation import (
    ConversationForm, MessageForm,
    EditMessageForm,
)
from application.login_manager import login_manager
from application.models import Conversation, Message
from application.permissions.decorators import is_normal_user, is_admin_user
from application.queries.category import (
    by_id_with_conversations,
    user_is_banned_from,
)
from application.queries.conversation import (
    by_id_with_messages_and_users,
    delete_conversation as delete_conversation_from_db, by_id,
)
from application.queries.message import (
    by_id as message_by_id,
    delete_message as delete_message_from_db,
    by_id_with_conversation as message_by_id_with_conversation,
)

community = Blueprint("community", __name__)


@community.route("/<int:id>")
@is_normal_user
def index(id):
    category = by_id_with_conversations(id)
    return render_template("community.html", community=category)


@community.route("/<int:community_id>/conversation", methods=["GET", "POST"])
@is_normal_user
def create_conversation(community_id):
    banned = user_is_banned_from(current_user.id, community_id)
    if banned:
        return login_manager.unauthorized()

    form = ConversationForm()
    if request.method == "POST" and form.validate_and_flash_errors():
        conversation = Conversation(
            user_id=current_user.id,
            category_id=community_id
        )
        form.save(conversation)
        return redirect(url_for("community.index", id=community_id))

    return render_template(
        "create_conversation.html",
        form=form,
        community_id=community_id
    )


@community.route("/conversation/<int:id>/delete")
@is_admin_user
def delete_conversation(id):
    conversation = by_id(id)
    category_id = conversation.category_id
    delete_conversation_from_db(id)
    return redirect(url_for("community.index", id=category_id))


@community.route("/conservation/<int:id>", methods=["GET", "POST"])
@is_normal_user
def conversation(id):
    form = MessageForm()

    if request.method == "POST" and form.validate_and_flash_errors():
        message = Message(user_id=current_user.id, conversation_id=id)
        form.save(message)
        form.message.data = ""

    conversation = by_id_with_messages_and_users(id)

    return render_template(
        "conversation.html",
        form=form,
        conversation=conversation
    )


@community.route("/message/<int:id>/edit", methods=["GET", "POST"])
@is_normal_user
def edit_message(id):
    message = message_by_id_with_conversation(id)
    if message.user_id != current_user.id:
        return login_manager.unauthorized()

    form = EditMessageForm(obj=message)

    if request.method == "POST" and form.validate_and_flash_errors():
        form.save(message)
        return redirect(
            url_for("community.conversation", id=message.conversation_id)
        )

    return render_template(
        "conversation.html",
        form=form,
        conversation=message.conversation,
        editing_message=message
    )


@community.route("/message/<int:id>/delete")
@is_admin_user
def delete_message(id):
    message = message_by_id(id)
    conversation_id = message.conversation_id
    delete_message_from_db(id)
    return redirect(url_for("community.conversation", id=conversation_id))
