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
    permitted = [
        'get_authenticated_user',
        'delete_user',
        'update_user',
        'create_review',
        'update_review',
        'delete_review',
        'get_authenticated_user_collections',
        'delete_collection',
        'create_collection',
        'create_comment',
        'delete_follow',
        'create_follow'
    ]


class Administrator(Scope):
    permitted = [
        'create_canteen',
        'update_canteen',
        'delete_canteen',
        'create_restaurant',
        'update_restaurant',
        'delete_restaurant',
        'create_food',
        'update_food',
        'delete_food'
    ]

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
