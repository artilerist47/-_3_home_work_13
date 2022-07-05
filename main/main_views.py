from flask import Blueprint, render_template

from utils import get_all_posts, get_post_by_id, get_posts_by_user, get_comments_by_post_id, get_len_comments_for_post

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@main_blueprint.get("/")
def main_page():
    """
    Открываем главную страницу со всеми постами
    """
    posts = get_all_posts()
    # return render_template("index.html", posts=posts)
    return render_template("all_posts.html", all_posts=posts)


@search_blueprint.get("/post/<int:pk>")
def search_post_by_id(pk):
    """
    Открываем конкретный пост
    """
    post = get_post_by_id(pk)
    comments = get_comments_by_post_id(pk)
    len_comments = get_len_comments_for_post(pk)
    return render_template("post_by_id.html", post_by_id=post, comments=comments, len_comments=len_comments)


@search_blueprint.get("/posts/<user_name>")
def search_post_by_user_name(user_name):
    """
    Открываем все посты конкретного пользователя
    """
    post = get_posts_by_user(user_name)
    return render_template("posts_by_user_name.html", posts_by_user_name=post)


# @search_blueprint.get("/search/")
# def main_page():
#     return render_template("search.html")


# @tag_blueprint.get("/tag/")
# def main_page():
#     return render_template("tag.html")
#
#
@bookmarks_blueprint.get("/bookmarks/")
def main_page():
    return render_template("bookmarks.html")

