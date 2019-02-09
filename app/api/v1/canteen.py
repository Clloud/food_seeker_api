"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from sqlalchemy import func

from app.models.canteen import Canteen
from app.models.picture import Picture
from app.validators.canteen import CanteenPostForm, CanteenPutForm
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from . import api


@api.route('/canteen/<int:canteen_id>', methods=['GET'])
def get_canteen(canteen_id):
    temp = db.session.query(Canteen).join(Picture).filter(Canteen.id == canteen_id).filter(
        Picture.canteen_id == canteen_id).all()
    return jsonify(temp)


@api.route('/campus/<int:campus_id>/canteens', methods=['GET'])
def get_canteens_by_campus(campus_id):
    temp = db.session.query(Canteen).join(Picture).filter(Canteen.campus_id == campus_id).filter(
        Picture.canteen_id == Canteen.id).all()
    return jsonify(temp)


@api.route('/canteen', methods=['POST'])
@auth.login_required
def create_canteen():
    form = CanteenPostForm().validate_for_api()
    with db.auto_commit():
        canteen = Canteen()
        canteen.set_attrs(form)
        db.session.add(canteen)
    return CreateSuccess()


@api.route('/canteen/<int:canteen_id>', methods=['PUT'])
@auth.login_required
def update_canteen(canteen_id):
    form = CanteenPutForm().validate_for_api()
    with db.auto_commit():
        canteen = Canteen.query.get_or_404(canteen_id)
        canteen.set_attrs(form)
        db.session.add(canteen)
    return UpdateSuccess()


@api.route('/canteen/<int:canteen_id>', methods=['DELETE'])
@auth.login_required
def delete_canteen(canteen_id):
    with db.auto_commit():
        canteen = Canteen.query.filter_by(id=canteen_id).first_or_404()
        canteen.delete()
    return DeleteSuccess()
