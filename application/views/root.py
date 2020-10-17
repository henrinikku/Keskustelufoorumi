from flask import Blueprint, render_template, request
from flask_login import current_user

from application.decorators.permissions import is_normal_user
from application.forms.search import SearchForm
from application.queries.category import readable_by_user
from application.queries.conversation import search_by_keyword

root = Blueprint("root", __name__)


@root.route("/", methods=["GET", "POST"])
@is_normal_user
def index():
    form = SearchForm()
    search = request.method == "POST" and form.validate_and_flash_errors()

    if search:
        conversations = search_by_keyword(form.keyword.data).all()
    else:
        conversations = []

    categories = readable_by_user(current_user).all()
    return render_template(
        "index.html",
        search=search,
        search_form=form,
        conversations=conversations,
        communities=categories
    )
