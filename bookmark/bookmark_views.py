import logging

from flask import Blueprint, render_template, abort

from bookmark.utils import get_all_bookmarks

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@bookmarks_blueprint.get("/all_bookmarks")
def bookmarks_page():
    """
    Открывает страницу с закладками
    """
    try:
        return render_template("all_bookmarks.html", all_bookmarks=get_all_bookmarks())
    except:
        logging.info("Problems opening the page(all_bookmarks)|Проблемы с открытием страницы(all_bookmarks)")
        return abort(500, "There was a problem with the server|На сервере произошли неполадки")
