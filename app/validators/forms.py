# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:18
'''
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.libs.error_code import ClientTypeError, ParameterError
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, field):
        try:
            client = ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='Invalid email address')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[
        DataRequired(), length(min=2, max=22)
    ])

    def validate_account(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ParameterError(message='Email address has been registered')


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])
