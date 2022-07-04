from flask import Flask
from main.views import main_blueprint, tag_blueprint, search_blueprint, bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)

app.run()