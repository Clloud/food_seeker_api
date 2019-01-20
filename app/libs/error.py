# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/15 19:43
'''
from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    message = 'Oops! The server encountered an internal error.'
    error_code = 999

    def __init__(self, message=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(message, None)

    def get_body(self, environ=None):
        body = dict(
            message=self.message,
            error_code=self.error_code,
            request_url=request.method + ' ' + self.get_url_without_param()
        )
        return json.dumps(body)

    @staticmethod
    def get_url_without_param():
        full_path = str(request.full_path)
        return full_path.split('?')[0]

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]