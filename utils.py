import json


def get_all_posts():
    """
    Читаем файл с постами
    """
    with open("data/posts.json", encoding="utf-8") as file:
        return json.load(file)


def get_all_comments():
    """
    Читаем файл с комментариями
    """
    with open("data/comments.json", encoding="utf-8") as file:
        return json.load(file)


def get_post_by_id(pk):
    """
    Получаем пост по ID поста
    """
    return [post for post in get_all_posts() if pk == post["pk"]]


def get_posts_by_user(user_name):
    """
    Получаем все посты конкретного пользователя
    """
    return [post for post in get_all_posts() if user_name == post["poster_name"].lower()]
# Функция должна вызывать ошибку ValueError если такого пользователя нет
# и пустой список, если у пользователя нет постов.


def get_comments_by_post_id(pk):
    """
    Получаем все комментарии для конкретного поста по ID поста
    """
    return [comment for comment in get_all_comments() if pk == comment["post_id"]]
# Возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет
# и пустой список, если у поста нет комментов.


def get_len_comments_for_post(comments_by_post_id):
    """
    Получаем количество комментариев для поста по ID поста
    """
    count = 0
    for comments in get_all_comments():
        if comments_by_post_id == comments["post_id"]:
            count += 1
    return count


def get_len_post(posts):
    """
    Получаем количество комментариев для поста по ID поста
    """
    count = 0
    for comments in get_all_comments():
        if posts == comments["pk"]:
            count += 1
    return count


def get_post_by_word(word):
    return [post for post in get_all_posts() if word in post["content"].lower()]
