# flask_blog/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views.entries import entry
from flask_blog.api.sample import api

app.register_blueprint(entry, url_prefix='/users')  # entryアプリケーションを登録
app.register_blueprint(api, url_prefix='/api')

from flask_blog.views import views

from flask_cors import CORS
CORS(app)
