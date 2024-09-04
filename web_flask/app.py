#!/usr/bin/python3
"""Flask App"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from web_flask.views import app_views
from web_flask.auth import app_auth

db = SQLAlchemy()
DB_NAME = 'database.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijk lmnopqrst'
app.config ['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

app.register_blueprint(app_views, url_prefix='/')
app.register_blueprint(app_auth, url_prefix='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
