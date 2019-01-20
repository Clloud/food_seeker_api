# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:06
'''
from . import api


@api.route('/comment', methods=['GET'])
def get_comment():
    return 'get_comment'