from flask import Blueprint, render_template, request

from utils import get_all_posts, get_post_by_id, get_posts_by_user, \
    get_comments_by_post_id, get_len_comments_for_post, get_post_by_word, \
    get_all_bookmarks, add_post_to_bookmark

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@main_blueprint.get("/")
def main_page():
    """
    Открывает главную страницу со всеми постами
    """
    posts = get_all_posts()
    len_bookmark = len(get_all_bookmarks())
    return render_template("all_posts.html", all_posts=posts, len_bookmark=len_bookmark)


@bookmarks_blueprint.get("/all_bookmarks")
def bookmarks_page():
    """
    Открывает страницу с закладками
    """
    posts_bookmark = get_all_bookmarks()
    return render_template("all_bookmarks.html", all_bookmarks=posts_bookmark)


@search_blueprint.get("/post/<int:pk>")
def search_post_by_id(pk):
    """
    Открывает конкретный пост
    """
    post = get_post_by_id(pk)
    comments = get_comments_by_post_id(pk)
    len_comments = get_len_comments_for_post(pk)
    return render_template("post_by_id.html", post_by_id=post, comments=comments, len_comments=len_comments)


@search_blueprint.get("/posts/<user_name>")
def search_post_by_user_name(user_name):
    """
    Открывает все посты конкретного пользователя
    """
    post = get_posts_by_user(user_name)
    return render_template("posts_by_user_name.html", posts_by_user_name=post)


@search_blueprint.get("/search/")
def search_page():
    """
    Ищет посты по вхождению слова
    """
    search_query = request.args.get("s", "").lower()
    posts = get_post_by_word(search_query)
    len_posts = len(posts)
    return render_template("search.html", query=search_query, posts=posts, len_posts=len_posts)


@bookmarks_blueprint.route("/add_bookmarks", methods=["POST"])
def add_bookmark():
    """
    Теоретически это должно быть добавлением закладки (но не работает)
    """

    poster_name = request.form.get("poster_name")
    poster_avatar = request.form.get("poster_avatar")
    pic = request.form.get("pic")
    content = request.form.get("content")
    views_count = request.form.get("views_count")
    likes_count = request.form.get("likes_count")
    pk = request.form.get("pk")

    post_to_bookmark = add_post_to_bookmark({"poster_name": poster_name,
                                             "poster_avatar": poster_avatar,
                                             "pic": pic,
                                             "content": content,
                                             "views_count": views_count,
                                             "likes_count": likes_count,
                                             "pk": pk
                                             })

    return render_template("all_bookmarks.html", post=post_to_bookmark)


# @bookmarks_blueprint.route("/bookmarks/add", methods=["POST"])
# def add_bookmark():
#
#     poster_name = request.form.get("poster_name")
#     poster_avatar = request.files.get("poster_avatar")
#     picture = request.files.get("picture")
#     content = request.form.get("content")
#     views_count = request.form.get("views_count")
#     likes_count = request.form.get("likes_count")
#     post_id = request.form.get("post_id")
#
#     post = add_post_to_bookmark({
#         "poster_name": poster_name,
#         "poster_avatar": poster_avatar,
#         "picture": picture,
#         "content": content,
#         "views_count": views_count,
#         "likes_count": likes_count,
#         "post_id": post_id,
#     })
#


# @tag_blueprint.get("/tag/")
# def main_page():
#     return render_template("tag.html")

