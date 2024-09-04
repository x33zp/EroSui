#!/usr/bin/python3
"""Flask App"""
from flask import Flask
from web_flask.views import app_views
from web_flask.auth import app_auth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijk lmnopqrst'


app.register_blueprint(app_views, url_prefix='/')
app.register_blueprint(app_auth, url_prefix='/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
