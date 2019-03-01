"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.api.v1 import api
from app.models.user import User
from app.models.review import Review
from app.models.food import Food
from app.models.restaurant import Restaurant
from app.validators.search import SearchRestaurantForm, SearchFoodForm, SearchReviewForm, SearchUserForm


def __sort_by_grade(r, order):
    _order_by = order + 'grade'
    _order_by2 = '-'+'create_time'
    return r.order_by(_order_by, _order_by2).custom_paginate()


def __sort_by_hot(r, order):
    _order_by = order + 'review_amount'
    return r.order_by(_order_by).custom_paginate()


def __sort_by_image(r, order):
    _order_by = order + 'image_amount'
    _order_by2 = '-' + 'create_time'
    return r.order_by(_order_by, _order_by2).custom_paginate()


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


@api.route('/search/reviews', methods=['GET'])
def search_reviews():
    form = SearchReviewForm().validate_for_api()
    q, sort, order = form.q.data, form.sort.data, form.order.data
    if sort == 'image':
        r = Review.query.filter(Review.content.contains(q),
                                 Review.image_amount > 0, Review.status == 1)
    else:
        r = Review.query.filter(Review.content.contains(q), Review.status == 1)
    promise = {
        'grade': __sort_by_grade,
        'new': __sort_by_new,
        'image': __sort_by_image
    }
    reviews = promise[sort](r, '+' if order == 'asc' else '-')
    reviews = [review.hide('restaurant') for review in reviews]
    return jsonify(reviews)


@api.route('/search/users', methods=['GET'])
def search_users():
    form = SearchUserForm().validate_for_api()
    sort, order = form.sort.data, form.order.data
    q = form.q.data.split(',')
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
