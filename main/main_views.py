from flask import Blueprint, render_template, request, redirect
import logging
from json import JSONDecodeError

from utils import get_all_posts, get_post_by_id, get_posts_by_user, \
    get_comments_by_post_id, get_len_comments_for_post, get_post_by_word, \
    get_all_bookmarks, add_post_to_bookmark, get_posts_by_tag

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@main_blueprint.get("/")
def main_page():
    """
    Открывает главную страницу со всеми постами
    """
    try:
        posts = get_all_posts()
    except FileNotFoundError:
        logging.error("File posts not found")
        return "Файл c постами не найден"
    except JSONDecodeError:
        logging.error("The file posts is corrupt or invalid")
        return "Файл с постами повреждён или не валиден"
    try:
        len_bookmark = len(get_all_bookmarks())
    except FileNotFoundError:
        logging.error("File bookmarks not found")
        return "Файл с закладками не найден"
    except JSONDecodeError:
        logging.error("The file bookmarks is corrupt or invalid")
        return "Файл с закладками повреждён или не валиден"
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
    try:
        comments = get_comments_by_post_id(pk)
    except FileNotFoundError:
        logging.error("File comments not found")
        return "Файл с комментариями не найден"
    except JSONDecodeError:
        logging.error("The file comments is corrupt or invalid")
        return "Файл с комментариями повреждён или не валиден"
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
    Добавляет закладки
    """
    poster_name = request.form.get("poster_name")
    poster_avatar = request.form.get("poster_avatar")
    pic = request.form.get("pic")
    content = request.form.get("content")
    views_count = request.form.get("views_count")
    likes_count = request.form.get("likes_count")
    pk = request.form.get("pk")

    add_post_to_bookmark({
        "poster_name": poster_name,
        "poster_avatar": poster_avatar,
        "pic": pic,
        "content": content,
        "views_count": views_count,
        "likes_count": likes_count,
        "pk": pk
    })

    return redirect("/", code=302)


@tag_blueprint.get("/tag/")
def tag_page():
    """
    Теоретически это должно быть поиском по тегам (но не работает)
    """
    posts_with_a_tag = get_posts_by_tag(tag="#")
    print(2, posts_with_a_tag)
    return render_template("tag.html", posts_with_a_tag=posts_with_a_tag)
