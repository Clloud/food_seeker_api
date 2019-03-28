"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify, g
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from app.models.invitation import Invitation
from app.validators.invitation import InvitationForm
from . import api


@api.route('/invitation', methods=['POST'])
@auth.login_required
def get_invitation():
    uid = g.user.uid
    form = InvitationForm().validate_for_api()
    Invitation.create_invitation(form, uid)
    return CreateSuccess()


@api.route('/invitation/<int:user_id>', methods=['GET'])
@auth.login_required
def get_invitation_by_user(user_id):
    invitation = Invitation.query.filter_by(user_id=user_id).custom_paginate()
    return jsonify(invitation)


@api.route('/invitation/<int:invitation_id>', methods=['GET'])
@auth.login_required
def get_invitation_by_id(invitation_id):
    invitation = Invitation.query.filter_by(id=invitation_id).first_or_404()
    invitation = invitation.hide('contact')
    return jsonify(invitation)
