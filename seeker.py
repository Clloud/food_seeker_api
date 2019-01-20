# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 20:59
'''
from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError


app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
    '''global error handler'''
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        return APIException(message=e.description,
                            code=e.code,
                            error_code=1007)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
