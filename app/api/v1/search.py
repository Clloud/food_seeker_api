"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, request

from app.api.v1 import api
from app.models.base import db
from app.models.comment import Comment
from app.models.food import Food
from app.models.restaurant import Restaurant
from app.validators.search import SearchRestaurantForm, SearchFoodForm, SearchCommentForm


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


@api.route('/search/foods', methods=['GET'])
def search_food():
    form = SearchFoodForm().validate_for_api()
    q = form.q.data
    sort = form.sort.data
    order = form.order.data
    foods = Food()
    if sort == 'best-match':
        foods = Food.query.filter(
            foods.name.contains(q),
            Food.status == 1).order_by().custom_paginate()
    elif sort == 'grade':
        foods = foods.search_sort_grade(q, order)
    elif sort == 'hot':
        foods = foods.search_sort_hot(q, order)
    return jsonify(foods)


@api.route('/search/comments', methods=['GET'])
def search_comments():
    form = SearchCommentForm().validate_for_api()
    q = form.q.data
    sort = form.sort.data
    order = form.order.data
    comments = Comment()
    if sort == 'best-match':
        comments = Food.query.filter(
            comments.name.contains(q),
            Comment.status == 1).order_by().custom_paginate()
    elif sort == 'image':
        comments = comments.search_sort_image(q, order)
    elif sort == 'grade':
        comments = comments.search_sort_grade(q, order)
    elif sort == 'poor':
        comments = comments.search_sort_poor(q, order)
    elif sort == 'new':
        comments = comments.search_sort_new(q, order)
    comments = [comment.hide('restaurant') for comment in comments]
    return jsonify(comments)
