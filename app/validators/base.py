# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/15 20:35
'''
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterError


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterError(message=self.errors)
        return self