# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 23:57
'''
from sqlalchemy import Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base, db
from app.libs.error_code import NotFound, AuthFailed


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24))
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

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