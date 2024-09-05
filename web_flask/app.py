#!/usr/bin/python3
"""Flask App"""
from flask import Flask
from web_flask.views import app_views
from web_flask.auth import app_auth
from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefghijk lmnopqrst'
    app.config ['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(app_auth, url_prefix='/')

    from models.test_model import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('EroSui/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')

            
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
