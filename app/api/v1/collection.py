"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import g

from app.libs.error_code import CreateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.user_collection import UserCollection
from . import api


@api.route('/collection/<int:restaurant_id>', methods=['POST'])
@auth.login_required
def create_collection(restaurant_id):
    uid = g.user.uid
    UserCollection.create_collection(uid, restaurant_id)
    return CreateSuccess()


@api.route('/collection/<int:restaurant_id>', methods=['DELETE'])
@auth.login_required
def delete_collection(restaurant_id):
    uid = g.user.uid
    UserCollection.delete_collection(uid, restaurant_id)
    return DeleteSuccess()
