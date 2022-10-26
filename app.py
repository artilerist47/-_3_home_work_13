import logging

from flask import Flask
from main.main_views import main_blueprint, search_blueprint, tag_blueprint
from bookmark.bookmark_views import bookmarks_blueprint
from bookmark.change_bookmarks import change_bookmarks
from api.api import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(change_bookmarks)
app.register_blueprint(api_blueprint)

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

if __name__ == "__main__":
    app.run()
