import logging

from flask import Blueprint, render_template, request, abort, redirect, jsonify

from utils import get_all_posts, get_post_by_id, get_posts_by_user, \
    get_comments_by_post_id, get_len_comments_for_post, get_post_by_word, \
    get_posts_by_tag, add_post_to_bookmark, remote_post_to_bookmark, get_all_bookmarks

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")
api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")


@main_blueprint.get("/")
def main_page():
    """
    Открывает главную страницу со всеми постами
    """
    posts = get_all_posts()
    len_bookmark = len(get_all_bookmarks())
    try:
        return render_template("all_posts.html", all_posts=posts, len_bookmark=len_bookmark)
    except:
        logging.info("Problems opening the page(all_posts)|Проблемы с открытием страницы(all_posts)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")


@search_blueprint.get("/post/<int:pk>")
def search_post_by_id(pk):
    """
    Открывает конкретный пост
    """
    post = get_post_by_id(pk)
    comments = get_comments_by_post_id(pk)
    len_comments = get_len_comments_for_post(pk)
    try:
        return render_template("post_by_id.html", post_by_id=post, comments=comments, len_comments=len_comments)
    except:
        logging.info("Problems opening the page(post_by_id)|Проблемы с открытием страницы(post_by_id)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")


@search_blueprint.get("/posts/<user_name>")
def search_post_by_user_name(user_name):
    """
    Открывает все посты конкретного пользователя
    """
    post = get_posts_by_user(user_name)
    try:
        return render_template("posts_by_user_name.html", posts_by_user_name=post)
    except:
        logging.info("Problems opening the page(posts_by_user_name)|Проблемы с открытием страницы(posts_by_user_name)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")


@search_blueprint.get("/search/")
def search_page():
    """
    Ищет посты по вхождению слова
    """
    search_query = request.args.get("s", "").lower()
    posts = get_post_by_word(search_query)
    len_posts = len(posts)
    try:
        return render_template("search.html", query=search_query, posts=posts, len_posts=len_posts)
    except:
        logging.info("Problems opening the page(search)|Проблемы с открытием страницы(search)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")


@tag_blueprint.get("/tag/")
def tag_page():
    """
    Теоретически это должно быть поиском по тегам (но не работает)
    """
    posts_with_a_tag = get_posts_by_tag(tag="#")
    print(2, posts_with_a_tag)
    return render_template("tag.html", posts_with_a_tag=posts_with_a_tag)


@bookmarks_blueprint.get("/all_bookmarks")
def bookmarks_page():
    """
    Открывает страницу с закладками
    """
    posts_bookmark = get_all_bookmarks()
    try:
        return render_template("all_bookmarks.html", all_bookmarks=posts_bookmark)
    except:
        logging.info("Problems opening the page(all_bookmarks)|Проблемы с открытием страницы(all_bookmarks)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")


@bookmarks_blueprint.route("/bookmarks/add_bookmarks", methods=["POST"])
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


@bookmarks_blueprint.route("/bookmarks/remove_bookmarks", methods=["POST"])
def remove_bookmark():
    """
    Удаляет закладки
    """
    poster_name = request.form.get("poster_name")
    poster_avatar = request.form.get("poster_avatar")
    pic = request.form.get("pic")
    content = request.form.get("content")
    views_count = request.form.get("views_count")
    likes_count = request.form.get("likes_count")
    pk = request.form.get("pk")

    remote_post_to_bookmark({
        "poster_name": poster_name,
        "poster_avatar": poster_avatar,
        "pic": pic,
        "content": content,
        "views_count": views_count,
        "likes_count": likes_count,
        "pk": pk
    })

    return redirect("/all_bookmarks", code=302)


@api_blueprint.get("/api/posts")
def read_posts():
    logging.info("Обращение ко всем постам")
    return jsonify(get_all_posts())


@api_blueprint.get("/api/posts/<int:pk>")
def read_post(pk):
    post = get_post_by_id(pk)
    logging.info("Обращение к одному посту")
    return jsonify(post[0])

