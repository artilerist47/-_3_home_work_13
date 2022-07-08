import logging

from flask import Flask
from main.main_views import main_blueprint, tag_blueprint, search_blueprint, bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.INFO)

if __name__ == "__main__":
    app.run()
