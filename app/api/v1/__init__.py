# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:40
'''
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/v1')

from app.api.v1 import user
from app.api.v1 import token
from app.api.v1 import review
from app.api.v1 import canteen
from app.api.v1 import restaurant
from app.api.v1 import food
from app.api.v1 import search
from app.api.v1 import collection
from app.api.v1 import feed
from app.api.v1 import image
from app.api.v1 import comment
from app.api.v1 import follow
from app.api.v1 import invitation
from app.api.v1 import invitation_response
