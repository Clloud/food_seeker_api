"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.restaurant import Restaurant
from app.validators.restaurant import RestaurantForm
from app.libs.error_code import CreateSuccess
from . import api


@api.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    return jsonify(restaurant)


@api.route('/canteen/<int:canteen_id>/restaurant', methods=['GET'])
def get_restaurant_by_canteen(canteen_id):
    # TODO bug
    restaurant = Restaurant.query.filter_by(id=canteen_id).all()
    return jsonify(restaurant)


@api.route('/restaurant', methods=['POST'])
def create_restaurant():
    # TODO 权限控制
    form = RestaurantForm().validate_for_api()
    Restaurant.create_Restaurant(form.name.data,
                              form.introduction.data,
                              form.canteen_id.data)
    return CreateSuccess()
