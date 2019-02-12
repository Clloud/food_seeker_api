"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.restaurant import Restaurant
from app.models.restaurant_image import RestaurantImage
from app.validators.restaurant import RestaurantUpdateForm, RestaurantCreateForm
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from . import api


@api.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    return jsonify(restaurant)


@api.route('/canteen/<int:canteen_id>/restaurants', methods=['GET'])
def get_restaurants_by_canteen(canteen_id):
    restaurants = Restaurant.query.filter_by(canteen_id=canteen_id).custom_paginate()
    return jsonify(restaurants)


@api.route('/restaurant', methods=['POST'])
@auth.login_required
def create_restaurant():
    form = RestaurantCreateForm().validate_for_api()
    with db.auto_commit():
        restaurant = Restaurant()
        restaurant.set_attrs(form)
        db.session.add(restaurant)
    return CreateSuccess()


@api.route('/restaurant/<int:restaurant_id>', methods=['PUT'])
@auth.login_required
def update_restaurant(restaurant_id):
    form = RestaurantUpdateForm().validate_for_api()
    with db.auto_commit():
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        restaurant.set_attrs(form)
        db.session.add(restaurant)
    return UpdateSuccess()


@api.route('/restaurant/<int:restaurant_id>', methods=['DELETE'])
@auth.login_required
def delete_restaurant(restaurant_id):
    with db.auto_commit():
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
        restaurant.delete()
    return DeleteSuccess()
