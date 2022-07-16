import logging
from flask import Blueprint, render_template, request, abort

from main.utils import get_all_posts, get_post_by_id, get_posts_by_user, \
    get_comments_by_post_id, get_len_comments_for_post, get_post_by_word, \
    get_posts_by_tag

from bookmark.utils import get_all_bookmarks

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")


@main_blueprint.get("/")
def main_page():
    """
    Открывает главную страницу со всеми постами
    """
    return render_template("all_posts.html", all_posts=get_all_posts(), len_bookmark=len(get_all_bookmarks()))


@search_blueprint.get("/post/<int:pk>")
def search_post_by_id(pk):
    """
    Открывает конкретный пост
    """
    if get_post_by_id(pk) is None:
        logging.info("No such post found|Такой пост не найден")
        return abort(404, ValueError("No such post found|Такой пост не найден"))
    else:
        return render_template("post_by_id.html", post_by_id=get_post_by_id(pk), comments=get_comments_by_post_id(pk),
                               len_comments=get_len_comments_for_post(pk))


@search_blueprint.get("/posts/<user_name>")
def search_post_by_user_name(user_name):
    """
    Открывает все посты конкретного пользователя
    """
    if get_posts_by_user(user_name) is None:
        logging.info("This user was not found|Такой пользователь не найден")
        return abort(404, ValueError("This user was not found|Такой пользователь не найден"))
    else:
        return render_template("posts_by_user_name.html", posts_by_user_name=get_posts_by_user(user_name))


@search_blueprint.get("/search/")
def search_page():
    """
    Ищет посты по вхождению слова
    """
    search_query = request.args.get("s", "").lower()
    return render_template("search.html", query=search_query, posts=get_post_by_word(search_query),
                           len_posts=len(get_post_by_word(search_query)))


@tag_blueprint.get("/tag/")
def tag_page():
    """
    Теоретически это должно быть поиском по тегам (но не работает)
    """
    posts_with_a_tag = get_posts_by_tag(tag="#")
    print(2, posts_with_a_tag)
    return render_template("tag.html", posts_with_a_tag=posts_with_a_tag)
