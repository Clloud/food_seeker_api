"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import g, jsonify

from app.libs.token_auth import auth
from app.models.message import Message
from . import api


@api.route('/user/messages', methods=['GET'])
@auth.login_required
def get_message_by_user():
    uid = g.user.uid
    messages = Message.query.filter_by(user_id=uid).all()
    return jsonify(messages)


@api.route('/message/<int:message_id>', methods=['GET'])
@auth.login_required
def get_message_by_id(message_id):
    message = Message.query.filter_by(id=message_id).first_or_404()
    message.change_state_of_message(message)
    return jsonify(message)
