from flask import Blueprint, render_template

from utils import get_all_posts

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


# @main_blueprint.get("/")
# def main_page():
#     return render_template("index.html")
@main_blueprint.get("/")
def main_page():
    posts = get_all_posts()
    # return render_template("index.html", posts=posts)
    return render_template("posts_list.html", posts=posts)


@search_blueprint.get("/search/")
def main_page():
    return render_template("search.html")


@tag_blueprint.get("/tag/")
def main_page():
    return render_template("tag.html")


@bookmarks_blueprint.get("/bookmarks/")
def main_page():
    return render_template("bookmarks.html")

