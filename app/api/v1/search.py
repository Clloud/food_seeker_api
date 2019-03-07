"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, request
from app.api.v1 import api
from app.models.user import User
from app.models.review import Review
from app.models.food import Food
from app.models.restaurant import Restaurant
from app.validators.search import SearchRestaurantForm, SearchFoodForm, SearchReviewForm, SearchUserForm


def __encapsulate_result(r_len, r):
    result = {
        'total_count': r_len,
        'items': r
    }
    return result


def __sort_by_grade(r, order):
    _order_by = order + 'grade'
    r = r.order_by(_order_by, '-create_time').custom_paginate(True)
    return __encapsulate_result(r.total, r.items)


def __sort_by_hot(r, order):
    _order_by = order + 'review_amount'
    r = r.order_by(_order_by, '-create_time').custom_paginate()
    return __encapsulate_result(r.total, r.items)


def __sort_by_new(r, order):
    _order_by = order + 'create_time'
    r = r.order_by(_order_by).custom_paginate()
    return __encapsulate_result(r.total, r.items)


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
    a = request
    form = SearchFoodForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    r = Food.query.filter(Food.name.contains(q), Food.status == 1)
    promise = {
        'grade': __sort_by_grade,
        'hot': __sort_by_hot
    }
    foods = promise[sort](r, '+' if order == 'asc' else '-')
    return jsonify(foods)


@api.route('/search/reviews', methods=['GET'])
def search_reviews():
    # TODO 重构
    form = SearchReviewForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    r = Review.query.filter(Review.content.contains(q), Review.status == 1)
    if sort == 'image':
        r = r.filter(Review.image_amount > 0)
    promise = {
        'grade': __sort_by_grade,
        'new': __sort_by_new
    }
    reviews = promise[sort](r, '+' if order == 'asc' else '-')
    reviews = [review.hide('restaurant') for review in reviews]
    return jsonify(reviews)


@api.route('/search/users', methods=['GET'])
def search_users():
    # TODO 重构
    form = SearchUserForm().validate_for_api()
    sort, order = form.sort.data, form.order.data
    q = form.q.data.split(' ')
    q = [item.split(':') for item in q]
    tempdict = {}
    for item in q:
        tempdict[item[0]] = item[1]
    q = tempdict
    standard = {
        'email': '',
        'mobile': ''
    }
    for key, value in q.items():
        standard[key] = value
    if standard['email'] == '':
        r = User.query.filter(User.mobile == standard['mobile'], User.status == 1)
    elif standard['mobile'] == '':
        r = User.query.filter(User.email == standard['email'], User.status == 1)
    else:
        r = User.query.filter(User.email == standard['email'], User.mobile == standard[
            'mobile'], User.status == 1)
    promise = {
        'new': __sort_by_new
    }
    users = promise[sort](r, '+' if order == 'asc' else '-')
    users = [user.hide('auth') for user in users]
    return jsonify(users)
