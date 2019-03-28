"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, g
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from app.models.invitation_reply import InvitationReply
from app.validators.invitation_reply import InvitationReplyForm
from . import api


@api.route('/invitation/<int:invitation_id>/reply', methods=['POST'])
@auth.login_required
def get_invitation_reply(invitation_id):
    uid = g.user.uid
    form = InvitationReplyForm().validate_for_api()
    InvitationReply.create_invitation_reply(form, invitation_id, uid)
    return CreateSuccess()


@api.route('/user/<int:user_id>/invitation/replies', methods=['GET'])
@auth.login_required
def get_invitation_reply_by_user(user_id):
    invitation_reply = InvitationReply.query.filter_by(user_id=user_id).custom_paginate()
    return jsonify(invitation_reply)


@api.route('/invitation/reply/<int:reply_id>', methods=['GET'])
@auth.login_required
def get_invitation_reply_id(reply_id):
    invitation_reply = InvitationReply.query.filter_by(id=reply_id).first_or_404()
    invitation_reply = invitation_reply.hide('contact')
    return jsonify(invitation_reply)
