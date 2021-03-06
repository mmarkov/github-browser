import os
from flask_sqlalchemy import SQLAlchemy
from logging import StreamHandler
from sys import stdout
from flask import Flask

db = SQLAlchemy()


def create_app():
    from api.users import users_api
    from views.index import index_view

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(users_api.blueprint, url_prefix='/api')
    app.register_blueprint(index_view)

    db.init_app(app)

    handler = StreamHandler(stdout)
    app.logger.addHandler(handler)
    return app
