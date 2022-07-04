from flask import Blueprint, render_template


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")

@main_blueprint.get("/")
def main_page():
    return render_template("index.html")


@search_blueprint.get("/search/")
def main_page():
    return render_template("search.html")


@tag_blueprint.get("/tag/")
def main_page():
    return render_template("tag.html")


@bookmarks_blueprint.get("/bookmarks/")
def main_page():
    return render_template("bookmarks.html")

