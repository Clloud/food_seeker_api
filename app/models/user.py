# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 23:57
'''
from flask import current_app
from sqlalchemy import Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base, db
from app.libs.error_code import NotFound, AuthFailed


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(32), unique=True)
    nickname = Column(String(24))
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128))
    mobile = Column(String(15), unique=True)
    avatar_id = Column(Integer)
    _avatar_url = Column('avatar_url', String(100))

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'email', 'nickname', 'mobile', 'avatar_url', 'auth', 'create_time']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @property
    def avatar_url(self):
        return current_app.config['IMAGE_URL_PREFIX'] + self._avatar_url \
            if self._avatar_url else self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify_by_email(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(message='User not found')
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid': user.id, 'scope': user.auth}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)