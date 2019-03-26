"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, g

from app.libs.error_code import CreateSuccess
from app.libs.token_auth import auth
from app.models.comment import Comment
from app.validators.comment import CommentForm
from . import api


@api.route('/review/<int:review_id>/comments', methods=['GET'])
def get_comments_by_review(review_id):
    comments = Comment.query.filter_by(review_id=review_id).order_by('-create_time').custom_paginate()
    return jsonify(comments)


@api.route('/comment/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comments = Comment.query.filter_by(id=comment_id).order_by('-create_time').first_or_404()
    return jsonify(comments)


@api.route('/comment', methods=['POST'])
@auth.login_required
def create_comment():
    form = CommentForm().validate_for_api()
    Comment.create_comment(form, g.user.uid)
    return CreateSuccess()
