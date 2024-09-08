#!/usr/bin/python3
"""Flask App"""
from flask import Flask
from web_flask.views import app_views
from web_flask.auth import app_auth
from flask_login import LoginManager
from models import storage
from models.user import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.register_blueprint(app_views)
app.register_blueprint(app_auth)

login_manager = LoginManager()
login_manager.login_view = 'app_auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return storage.get(User, id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
