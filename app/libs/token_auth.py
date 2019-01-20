# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/16 17:16
'''
from collections import namedtuple
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_permitted

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # save user information to global variable 'g'
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(message='Invalid token',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(message='Token has expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']

    if not is_permitted(scope, request.endpoint):
        raise Forbidden()
    return User(uid, ac_type, scope)