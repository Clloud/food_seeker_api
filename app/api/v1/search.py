"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.api.v1 import api
from app.models.base import db
from app.models.comment import Comment
from app.models.food import Food
from app.models.restaurant import Restaurant
from app.validators.search import SearchRestaurantForm, SearchFoodForm, SearchCommentForm


def __sort_by_grade(r, order):
    _order_by = order + 'grade'
    return r.order_by(_order_by).custom_paginate()


def __sort_by_hot(r, order):
    _order_by = order + 'comment_amount'
    return r.order_by(_order_by).custom_paginate()


def __sort_by_image(r, order):
    #_order_by = order + 'images'
    #return r.order_by(_order_by).custom_paginate()
    pass


def __sort_by_new(r, order):
    _order_by = order + 'create_time'
    return r.order_by(_order_by).custom_paginate()


@api.route('/search/restaurants', methods=['GET'])
def search_restaurants():
    form = SearchRestaurantForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    r = Restaurant.query.filter(Restaurant.name.contains(q),
                                Restaurant.status == 1)
    promise = {
        'grade': __sort_by_grade,
        'hot': __sort_by_hot
    }
    restaurants = promise[sort](r, '+' if order == 'asc' else '-')
    return jsonify(restaurants)


@api.route('/search/foods', methods=['GET'])
def search_food():
    form = SearchFoodForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    r = Food.query.filter(Food.name.contains(q), Food.status == 1)
    promise = {
        'grade': __sort_by_grade,
        'hot': __sort_by_hot
    }
    foods = promise[sort](r, '+' if order == 'asc' else '-')
    return jsonify(foods)


@api.route('/search/comments', methods=['GET'])
def search_comments():
    form = SearchCommentForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    r = Comment.query.filter(Comment.content.contains(q), Comment.status == 1)
    promise = {
        'grade': __sort_by_grade,
        'new': __sort_by_new,
        'image': __sort_by_image
    }
    comments = promise[sort](r, '+' if order == 'asc' else '-')
    comments = [comment.hide('restaurant') for comment in comments]
    return jsonify(comments)
