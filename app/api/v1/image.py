"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request, jsonify

from app.libs.error_code import CreateSuccess
from app.models.base import db
from app.models.canteen_image import CanteenImage
from app.models.review_image import ReviewImage
from app.models.food_image import FoodImage
from app.models.image import Image
from app.models.restaurant_image import RestaurantImage
from . import api


@api.route('/image', methods=['POST'])
def create_image():
    image = request.files.get('image')
    result = Image.save_image(image)
    return jsonify(result)


@api.route('/canteen/<int:canteen_id>/image', methods=['POST'])
def create_canteen_image(canteen_id):
    image = request.files.get('image')
    result = Image.save_image(image)
    with db.auto_commit():
        canteen_image = CanteenImage()
        canteen_image.canteen_id = canteen_id
        canteen_image.image_id = result["image_id"]
        db.session.add(canteen_image)
    return CreateSuccess()


@api.route('/restaurant/<int:restaurant_id>/image', methods=['POST'])
def create_restaurant_image(restaurant_id):
    image = request.files.get('image')
    result = Image.save_image(image)
    with db.auto_commit():
        restaurant_image = RestaurantImage()
        restaurant_image.restaurant_id = restaurant_id
        restaurant_image.image_id = result["image_id"]
        db.session.add(restaurant_image)
    return CreateSuccess()


@api.route('/food/<int:food_id>/image', methods=['POST'])
def create_food_image(food_id):
    image = request.files.get('image')
    result = Image.save_image(image)
    with db.auto_commit():
        food_image = FoodImage()
        food_image.food_id = food_id
        food_image.image_id = result["image_id"]
        db.session.add(food_image)
    return CreateSuccess()


@api.route('/comment/<int:comment_id>/image', methods=['POST'])
def create_comment_image(comment_id):
    image = request.files.get('image')
    result = Image.save_image(image)
    with db.auto_commit():
        comment_image = ReviewImage()
        comment_image.comment_id = comment_id
        comment_image.image_id = result["image_id"]
        db.session.add(comment_image)
    return CreateSuccess()
