import json
import logging
from flask import abort
from json import JSONDecodeError


def get_all_bookmarks():
    """
    Читаем файл с закладками
    """
    try:
        with open("data/bookmarks.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("File bookmarks not found|Файл с закладками не найден")
        return abort(404, ValueError("File bookmarks not found|Файл с закладками не найден"))
    except JSONDecodeError:
        logging.info("The file bookmarks is corrupt or invalid|Файл с закладками повреждён или не валиден")
        return abort(500,
                     ValueError("The file bookmarks is corrupt or invalid|Файл с закладками повреждён или не валиден"))


def add_post_to_bookmark(post_bookmark):
    """
    Функция добавления закладок
    """
    add_post = get_all_bookmarks()
    if post_bookmark not in add_post:
        add_post.append(post_bookmark)
        with open("data/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(add_post, file, ensure_ascii=False)


def remote_post_to_bookmark(post_bookmark):
    """
    Функция удаления закладок
    """
    remove_post = get_all_bookmarks()
    if post_bookmark in remove_post:
        remove_post.remove(post_bookmark)
        with open("data/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(remove_post, file, ensure_ascii=False)
