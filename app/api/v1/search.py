"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, request

from app.api.v1 import api
from app.models.base import db
from app.models.restaurant import Restaurant
from app.validators.search import SearchRestaurantForm


@api.route('/search/restaurants', methods=['GET'])
def search_restaurant():
    form = SearchRestaurantForm().validate_for_api()
    q = form.q.data
    sort = form.sort.data
    order = form.order.data
    restaurants = Restaurant()
    if sort == 'best-match':
        restaurants = Restaurant.query.filter(
            Restaurant.name.contains(q),
            Restaurant.status == 1).order_by().custom_paginate()
    elif sort == 'grade':
        restaurants = restaurants.search_sort_grade(q, order)
    elif sort == 'hot':
        restaurants = restaurants.search_sort_hot(q, order)
    return jsonify(restaurants)
