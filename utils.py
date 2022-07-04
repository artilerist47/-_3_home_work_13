import json


def get_all_posts():
    with open("data/posts.json", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_user(user_name):
    result = [post for post in get_all_posts() if user_name in post["poster_name"].lower()]
    return result
# Функция должна вызывать ошибку ValueError если такого пользователя нет
# и пустой список, если у пользователя нет постов.


def get_comments_by_post_id(post_id):
    pass
# Возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет
# и пустой список, если у поста нет комментов.
#


def search_for_posts(query):
    pass


def get_post_by_pk(pk):
    result = [post for post in get_all_posts() if pk in post["pk"].lower()]
    return result
