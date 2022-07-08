import json
import logging
from json import JSONDecodeError


def get_all_posts():
    """
    Читаем файл с постами
    """
    try:
        with open("data/posts.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("File posts not found")
        return "Файл c постами не найден"
    except JSONDecodeError:
        logging.error("The file posts is corrupt or invalid")
        return "Файл с постами повреждён или не валиден"


def get_all_comments():
    """
    Читаем файл с комментариями
    """
    try:
        with open("data/comments.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("File comments not found")
        return "Файл с комментариями не найден"
    except JSONDecodeError:
        logging.error("The file comments is corrupt or invalid")
        return "Файл с комментариями повреждён или не валиден"


def get_all_bookmarks():
    """
    Читаем файл с закладками
    """
    try:
        with open("data/bookmarks.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("File bookmarks not found")
        return "Файл с закладками не найден"
    except JSONDecodeError:
        logging.error("The file bookmarks is corrupt or invalid")
        return "Файл с закладками повреждён или не валиден"


def get_post_by_id(pk):
    """
    Получаем пост по ID поста
    """
    return [post for post in get_all_posts() if pk == post["pk"]]


def get_posts_by_user(user_name):
    """
    Получаем все посты конкретного пользователя
    """
    try:
        return [post for post in get_all_posts() if user_name == post["poster_name"].lower()]
    except ValueError:
        return "Такой пользователь не найден"


def get_comments_by_post_id(pk):
    """
    Получаем все комментарии для конкретного поста по ID поста
    """
    try:
        return [comment for comment in get_all_comments() if pk == comment["post_id"]]
    except ValueError:
        return "Такого поста нет"


def get_len_comments_for_post(comments_by_post_id):
    """
    Получаем количество комментариев для поста по ID поста
    """
    count = 0
    for comments in get_all_comments():
        if comments_by_post_id == comments["post_id"]:
            count += 1
    return count


def get_post_by_word(word):
    """
    Возвращает список постов по ключевому слову
    """
    return [post for post in get_all_posts() if word in post["content"].lower()]


def add_post_to_bookmark(post_bookmark):
    """
    Функция добавления закладок (временно не работает, добавляет все строки null)
    """
    add_post = get_all_bookmarks()
    add_post.append(post_bookmark)
    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(add_post, file, ensure_ascii=False)

