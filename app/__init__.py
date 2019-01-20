# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:02
'''
from app.app import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    register_plugin(app)

    return app


def register_blueprint(app):
    from app.api.v1 import api
    app.register_blueprint(api)


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


