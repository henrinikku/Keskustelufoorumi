from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user

from application.decorators.permissions import is_normal_user, is_admin_user
from application.forms.conversation import ConversationForm, MessageForm
from application.models import Conversation, Message
from application.queries.category import by_id_with_conversations
from application.queries.conversation import (
    by_id_with_messages_and_users,
    delete_conversation as delete_conversation_from_db, by_id,
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
