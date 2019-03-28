"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, g
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from app.models.invitation_response import InvitationResponse
from app.validators.invitation_response import InvitationResponseForm
from . import api


@api.route('/invitation_response', methods=['POST'])
@auth.login_required
def get_invitation_response():
    uid = g.user.uid
    form = InvitationResponseForm().validate_for_api()
    InvitationResponse.create_invitation_response(form, uid)
    return CreateSuccess()


@api.route('/user/<int:user_id>/invitation_responses', methods=['GET'])
@auth.login_required
def get_invitation_response_by_user(user_id):
    invitation_response = InvitationResponse.query.filter_by(user_id=user_id).custom_paginate()
    return jsonify(invitation_response)


@api.route('/invitation_response/<int:invitation_response_id>', methods=['GET'])
@auth.login_required
def get_invitation_response_id(invitation_response_id):
    invitation_response = InvitationResponse.query.filter_by(id=invitation_response_id).first_or_404()
    invitation_response = invitation_response.hide('contact')
    return jsonify(invitation_response)
