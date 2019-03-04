# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:02
'''
from app.app import Flask
from app.config.setting import config
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app, supports_credentials=True)

    register_blueprint(app)
    register_plugin(app)

    return app


def register_blueprint(app):
    from app.api.v1 import api
    app.register_blueprint(api)


def register_plugin(app):
    from app.models.base import db
    from flask_migrate import Migrate

    # register sqlalchemy
    db.init_app(app)

    # create all tables defined by models
    with app.app_context():
        db.create_all()

    # use flask-migrate to keep track of database changes
    migrate = Migrate(app, db)


