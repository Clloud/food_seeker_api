"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.canteen import Canteen
from app.validators.canteen import CanteenForm
from app.libs.error_code import CreateSuccess
from app.libs.token_auth import auth
from app.models.base import db
from . import api


@api.route('/canteen/<int:canteen_id>', methods=['GET'])
def get_canteen(canteen_id):
    canteen = Canteen.query.filter_by(id=canteen_id).first_or_404()
    return jsonify(canteen)


@api.route('/campus/<int:campus_id>/canteens', methods=['GET'])
def get_canteens_by_campus(campus_id):
    canteens = Canteen.query.filter_by(campus_id=campus_id).custom_paginate()
    return jsonify(canteens)


@api.route('/canteen', methods=['POST'])
@auth.login_required
def create_canteen():
    form = CanteenForm().validate_for_api()
    with db.auto_commit():
        canteen = Canteen()
        canteen.set_attrs(form)
        db.session.add(canteen)
    return CreateSuccess()
