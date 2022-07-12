import json
import logging
from flask import abort
from json import JSONDecodeError


def get_all_posts():
    """
    Читаем файл с постами
    """
    try:
        with open("data/posts.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("File posts not found|Файл с постами не найден")
        return abort(404, ValueError("File posts not found|файл с постами не найден"))
    except JSONDecodeError:
        logging.info("The file posts is corrupt or invalid|Файл с постами повреждён или не валиден")
        return abort(500, ValueError("The file posts is corrupt or invalid|Файл с постами повреждён или не валиден"))


def get_all_comments():
    """
    Читаем файл с комментариями
    """
    try:
        with open("data/comments.json", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("File comments not found|Файл с комментариями не найден")
        return abort(404, ValueError("File comments not found|Файл с комментариями не найден"))
    except JSONDecodeError:
        logging.info("The file comments is corrupt or invalid|Файл с комментариями повреждён или не валиден")
        return abort(500, ValueError(
            "The file comments is corrupt or invalid|Файл с комментариями повреждён или не валиден"))


def get_post_by_id(pk):
    """
    Получаем пост по ID поста
    """
    post = [post for post in get_all_posts() if pk == post["pk"]]
    if not post:
        logging.info("No such post found|Такой пост не найден")
        return abort(404, ValueError("No such post found|Такой пост не найден"))
    else:
        return post


def get_posts_by_user(user_name):
    """
    Получаем все посты конкретного пользователя
    """
    post = [post for post in get_all_posts() if user_name == post["poster_name"].lower()]
    if not post:
        logging.info("This user was not found|Такой пользователь не найден")
        return abort(404, ValueError("This user was not found|Такой пользователь не найден"))
    else:
        return post


def get_comments_by_post_id(pk):
    """
    Получаем все комментарии для конкретного поста по ID поста
    """
    return [comment for comment in get_all_comments() if pk == comment["post_id"]]


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


def get_posts_by_tag(tag):
    """
    Получает все посты с указанным тегом (он получает пустой список)
    """
    print(1, [post for post in get_all_posts() if tag in post["content"]])
    return [post for post in get_all_posts() if tag in post["content"]]


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
