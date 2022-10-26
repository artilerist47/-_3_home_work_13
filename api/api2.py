# файл тестовый. не уверен как его правильно писать
from flask import Flask, jsonify
import json

app = Flask(__name__)


def get_all_posts_for_test():
    with open("data/posts.json", encoding="utf-8") as file:
        return json.load(file)


@app.route("/api/posts")
def read_posts():
    data = get_all_posts_for_test()
    return jsonify(data)


@app.route("/api/posts/<int:pk>")
def read_post(pk):
    post = [post for post in get_all_posts_for_test() if pk == post["pk"]]
    return jsonify(post[0])


if __name__ == "__main__":
    app.run()
