import logging

from flask import render_template, abort, Blueprint

from bookmark.utils import get_all_bookmarks

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


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
