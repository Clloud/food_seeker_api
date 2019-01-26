# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/17 17:08
'''
from app.libs.enums import ScopeEnum


class Scope:
    permitted = []
    forbidden = []

    def __add__(self, other):
        self.permitted = self.permitted + other.permitted
        self.permitted = list(set(self.permitted))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class User(Scope):
    permitted = ['get_user', 'delete_user']


class Administrator(Scope):
    permitted = []

    def __init__(self):
        self + User()


def is_permitted(scope, endpoint):
    key = str(ScopeEnum(scope).name).title()
    scope = globals()[key]()
    endpoint = endpoint.split('.')[1]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.permitted:
        return True

    return False
