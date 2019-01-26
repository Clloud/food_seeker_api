# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:40
'''
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/v1')

from app.api.v1 import user
from app.api.v1 import comment
from app.api.v1 import client
from app.api.v1 import token
