from flask import request, redirect, Blueprint

from bookmark.utils import add_post_to_bookmark, remote_post_to_bookmark

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


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