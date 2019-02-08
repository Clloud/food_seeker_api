# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:06
'''
from flask import jsonify, g
from app.models.comment import Comment
from app.validators.comment import CommentPostForm, CommentPutForm
from app.libs.error_code import CreateSuccess, DeleteSuccess, UpdateSuccess
from app.models.base import db
from app.libs.token_auth import auth
from . import api


@api.route('/comment/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first_or_404()
    return jsonify(comment)


@api.route('/restaurant/<int:restaurant_id>/comments', methods=['GET'])
def get_comments_by_restaurant(restaurant_id):
    comments = Comment.query.filter_by(restaurant_id=restaurant_id).custom_paginate()
    return jsonify(comments)


@api.route('/user/<int:user_id>/comments', methods=['GET'])
def get_comments_by_user(user_id):
    comments = Comment.query.filter_by(user_id=user_id).custom_paginate()
    return jsonify(comments)


@api.route('/comment', methods=['POST'])
@auth.login_required
def create_comment():
    form = CommentPostForm().validate_for_api()
    with db.auto_commit():
        comment = Comment()
        comment.set_attrs(form)
        db.session.add(comment)
    return CreateSuccess()


@api.route('/comment/<int:comment_id>', methods=['PUT'])
@auth.login_required
def update_comment(comment_id):
    form = CommentPutForm().validate_for_api()
    with db.auto_commit():
        comment = Comment.query.get_or_404(comment_id)
        comment.set_attrs(form)
        db.session.add(comment)
    return UpdateSuccess()


@api.route('/comment/<int:comment_id>', methods=['DELETE'])
@auth.login_required
def delete_comment(comment_id):
    user_id = g.user.uid
    with db.auto_commit():
        comment = Comment.query.filter_by(user_id=user_id, id=comment_id).first_or_404()
        comment.delete()
    return DeleteSuccess()
