# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:42
'''
from flask import jsonify, g, current_app
from app.models.user import User
from app.libs.token_auth import auth
from app.models.base import db
from app.libs.error_code import DeleteSuccess, UpdateSuccess, Success, NotFound
from app.validators.user import UserUpdateForm, ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from . import api


@api.route('/user/<int:uid>', methods=['GET'])
def get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    user = user.hide('auth')
    return jsonify(user)


@api.route('/user', methods=['GET'])
@auth.login_required
def get_authenticated_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/user', methods=['POST'])
def create_user():
    # TODO 修正不能自动写入时间戳的问题
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


@api.route('/user', methods=['PUT'])
@auth.login_required
def update_user():
    form = UserUpdateForm().validate_for_api()
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.get_or_404(uid)
        user.nickname = form.nickname.data
        user.mobile = form.mobile.data
        user.email = form.email.data
        db.session.add(user)
    return UpdateSuccess()


@api.route('/user', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
