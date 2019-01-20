# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:34
'''
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    '''overwrite default function to serialize object'''
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    '''replace original flask JSONEncoder'''
    json_encoder = JSONEncoder


