# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/15 20:25
'''
from app.libs.error import APIException


class Success(APIException):
    code = 200
    message = 'OK'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202
    message = 'Deleted'
    error_code = 0


class ServerError(APIException):
    code = 500
    message = 'Oops! The server encountered an internal error.'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    message = 'Invalid client type'
    error_code = 1006


class ParameterError(APIException):
    code = 400
    message = 'Invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    message = 'Resource not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    message = 'Authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    message = 'Not authorized to perform the operation'
    error_code = 1004