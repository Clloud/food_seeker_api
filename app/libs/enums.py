# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:15
'''
from enum import Enum

class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

class ScopeEnum(Enum):
    USER = 1
    ADMINISTRATOR = 2