"""
Enjoy The Code!
"""
#__Auther__:__blank__
import os
from flask import request, make_response, jsonify, current_app
from app.libs.error_code import CreateSuccess, FormatError, ContentError, SizeError
from app.models.base import db
from app.models.picture import Picture
from app.validators.picture import PictureForm
from . import api


"""@api.route('/picture/<string:filename>', methods=['GET'])
def get_picture(filename):
    file_dir = os.path.join(basedir, "\\food_seeker_api\\app\\pictures")
    if filename:
        image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/png'
        return response"""


@api.route('/picture/<int:picture_id>', methods=['GET'])
def get_picture(picture_id):
    picture = Picture.query.filter_by(id=picture_id).first_or_404()
    return jsonify(picture)


@api.route('/user/<int:user_id>/pictures', methods=['GET'])
def get_pictures_by_user(user_id):
    pictures = Picture.query.filter_by(user_id=user_id).first_or_404()
    return jsonify(pictures)


@api.route('/canteen/<int:canteen_id>/pictures', methods=['GET'])
def get_pictures_by_canteen(canteen_id):
    pictures = Picture.query.filter_by(canteen_id=canteen_id).first_or_404()
    return jsonify(pictures)


@api.route('/restaurant/<int:restaurant_id>/pictures', methods=['GET'])
def get_pictures_by_restaurant(reataurant_id):
    pictures = Picture.query.filter_by(reataurant_id=reataurant_id).first_or_404()
    return jsonify(pictures)


@api.route('/food/<int:food_id>/pictures', methods=['GET'])
def get_pictures_by_food(food_id):
    pictures = Picture.query.filter_by(food_id=food_id).first_or_404()
    return jsonify(pictures)


@api.route('/comment/<int:comment_id>/pictures', methods=['GET'])
def get_pictures_by_comment(comment_id):
    pictures = Picture.query.filter_by(comment_id=comment_id).first_or_404()
    return jsonify(pictures)


@api.route('/picture', methods=['POST'])
def create_photo():
    img = request.files.get('picture')
    picture = Picture()
    if not img:
        return ContentError()
    if not picture.allowed_file(img.filename):
        return FormatError()
    form = PictureForm().validate_for_api()
    img.filename = picture.create_unique_name()
    picture.save_picture(img)
    with db.auto_commit():
        picture.set_attrs(form)
        picture.url = img.filename
        db.session.add(picture)
    return CreateSuccess()
