import logging

from flask import Blueprint, jsonify

from main.utils import get_all_posts, get_post_by_id


api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")


@api_blueprint.get("/api/posts")
def read_posts():
    logging.info("Обращение ко всем постам")
    data = get_all_posts()
    return jsonify(data)


@api_blueprint.get("/api/posts/<int:pk>")
def read_post(pk):
    post = get_post_by_id(pk)
    logging.info("Обращение к одному посту")
    return jsonify(post[0])

