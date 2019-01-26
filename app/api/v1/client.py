# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:13
'''
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.error_code import Success
from . import api


@api.route('/client/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.nickname.data,
        form.account.data,
        form.secret.data
    )