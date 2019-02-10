"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.food import Food
from app.validators.food import FoodUpdateForm, FoodCreateForm
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from . import api


@api.route('/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = Food.query.filter_by(id=food_id).first_or_404()
    return jsonify(food)


@api.route('/restaurant/<int:restaurant_id>/foods', methods=['GET'])
def get_foods_by_restaurant(restaurant_id):
    foods = Food.query.filter_by(restaurant_id=restaurant_id).custom_paginate()
    return jsonify(foods)


@api.route('/food', methods=['POST'])
@auth.login_required
def create_food():
    form = FoodCreateForm().validate_for_api()
    with db.auto_commit():
        food = Food()
        food.set_attrs(form)
        db.session.add(food)
    return CreateSuccess()


@api.route('/food/<int:food_id>', methods=['PUT'])
@auth.login_required
def update_food(food_id):
    form = FoodUpdateForm().validate_for_api()
    with db.auto_commit():
        food = Food.query.get_or_404(food_id)
        food.set_attrs(form)
        db.session.add(food)
    return UpdateSuccess()


@api.route('/food/<int:food_id>', methods=['DELETE'])
@auth.login_required
def delete_food(food_id):
    with db.auto_commit():
        food = Food.query.filter_by(id=food_id).first_or_404()
        food.delete()
    return DeleteSuccess()
