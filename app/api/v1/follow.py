"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import g

from app.libs.error_code import CreateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.user_follow import UserFollow
from . import api


@api.route('/follow/<int:following_id>', methods=['POST'])
@auth.login_required
def create_follow(following_id):
    uid = g.user.uid
    UserFollow.create_follow(uid, following_id)
    return CreateSuccess()


@api.route('/follow/<int:following_id>', methods=['DELETE'])
@auth.login_required
def delete_follow(following_id):
    uid = g.user.uid
    UserFollow.delete_follow(uid, following_id)
    return DeleteSuccess()
