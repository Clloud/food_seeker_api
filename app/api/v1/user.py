# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 21:42
'''
from flask import jsonify, g
from app.models.user import User
from app.libs.token_auth import auth
from app.models.base import db
from app.libs.error_code import DeleteSuccess, PostSuccess
from app.validators.forms import UserUpdateForm
from . import api


@api.route('/user', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/uesr', methods=['PUT'])
@auth.login_required
def update_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    form = UserUpdateForm().validate_for_api()
    form.setattr()
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        db.session.update(user)
    return PostSuccess()


@api.route('/user', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
