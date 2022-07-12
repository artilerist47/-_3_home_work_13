from flask import Blueprint, request, redirect

from bookmark.utils import add_post_to_bookmark, remote_post_to_bookmark

change_bookmarks = Blueprint("change_bookmarks", __name__, template_folder="templates")


@change_bookmarks.route("/bookmarks/add_bookmarks", methods=["POST"])
def add_bookmark():
    """
    Добавляет закладки
    """
    add_post_to_bookmark({
        "poster_name": request.form.get("poster_name"),
        "poster_avatar": request.form.get("poster_avatar"),
        "pic": request.form.get("pic"),
        "content": request.form.get("content"),
        "views_count": request.form.get("views_count"),
        "likes_count": request.form.get("likes_count"),
        "pk": request.form.get("pk")
    })

    return redirect("/", code=302)


@change_bookmarks.route("/bookmarks/remove_bookmarks", methods=["POST"])
def remove_bookmark():
    """
    Удаляет закладки
    """
    remote_post_to_bookmark({
        "poster_name": request.form.get("poster_name"),
        "poster_avatar": request.form.get("poster_avatar"),
        "pic": request.form.get("pic"),
        "content": request.form.get("content"),
        "views_count": request.form.get("views_count"),
        "likes_count": request.form.get("likes_count"),
        "pk": request.form.get("pk")
    })

    return redirect("/all_bookmarks", code=302)
