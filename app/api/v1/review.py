# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/14 22:06
'''
from flask import jsonify, g
from app.models.review import Review
from app.models.review_image import ReviewImage
from app.models.campus import Campus
from app.validators.review import ReviewCreateForm, ReviewUpdateForm
from app.libs.error_code import CreateSuccess, DeleteSuccess, UpdateSuccess, Forbidden
from app.models.base import db
from app.libs.token_auth import auth
from . import api


@api.route('/review/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.filter_by(id=review_id).first_or_404()
    return jsonify(review)


@api.route('/restaurant/<int:restaurant_id>/reviews', methods=['GET'])
def get_reviews_by_restaurant(restaurant_id):
    reviews = Review.query.filter_by(restaurant_id=restaurant_id).custom_paginate()
    reviews = [review.hide('restaurant') for review in reviews]
    return jsonify(reviews)


@api.route('/user/<int:user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    reviews = Review.query.filter_by(user_id=user_id).custom_paginate()
    reviews = [review.hide('restaurant') for review in reviews]
    return jsonify(reviews)


@api.route('/review', methods=['POST'])
@auth.login_required
def create_review():
    form = ReviewCreateForm().validate_for_api()
    Review.create_review(form, g.user.uid)
    return CreateSuccess()


@api.route('/review/<int:review_id>', methods=['PUT'])
@auth.login_required
def update_review(review_id):
    form = ReviewUpdateForm().validate_for_api()
    review = Review.query.get_or_404(review_id)
    if g.user.uid != review.user_id:
        raise Forbidden()

    with db.auto_commit():
        review.set_attrs(form)
        db.session.add(review)
    return UpdateSuccess()


@api.route('/review/<int:review_id>', methods=['DELETE'])
@auth.login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    if g.user.uid != review.user_id:
        raise Forbidden()

    with db.auto_commit():
        review.delete()
    return DeleteSuccess()
