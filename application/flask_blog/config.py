# flask_blog/config.py

SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATION = True
DEBUG = True
SECRET_KEY = 'secret key' # このsecret keyを使って、session情報が暗号化される
USERNAME = 'john'
PASSWORD = 'due123'
