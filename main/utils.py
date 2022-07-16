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
    post_by_id = [post for post in get_all_posts() if pk == post["pk"]]
    if not post_by_id:
        return None
    else:
        return post_by_id


def get_posts_by_user(user_name):
    """
    Получаем все посты конкретного пользователя
    """
    posts_by_user_name = [post for post in get_all_posts() if user_name == post["poster_name"].lower()]
    if not posts_by_user_name:
        return None
    else:
        return posts_by_user_name


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
