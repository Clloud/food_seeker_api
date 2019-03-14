"""
Enjoy The Code!
"""
#__Auther__:__blank__
import random

from flask import jsonify

from app.models.banner import Banner
from app.models.food import Food
from app.models.restaurant import Restaurant
from app.models.review import Review
from . import api


@api.route('/feed/restaurants', methods=['GET'])
def feed_restaurants():
    restaurants = Restaurant.query.filter_by().order_by('-grade').custom_paginate()
    return jsonify(restaurants)


@api.route('/feed/foods', methods=['GET'])
def feed_foods():
    foods = Food.query.filter_by().order_by('-grade').custom_paginate()
    return jsonify(foods)


@api.route('/feed/reviews', methods=['GET'])
def feed_reviews():
    reviews = Review.query.filter_by().order_by('-create_time').custom_paginate()
    reviews = [review.append('restaurant_id').hide('restaurant') for review in reviews]
    return jsonify(reviews)


@api.route('/feed/banners', methods=['GET'])
def feed_banners():
    banner = Banner.query.filter_by().all()
    banner = random.sample(banner, 3)
    banners = [i.image for i in banner]
    return jsonify(banners)
