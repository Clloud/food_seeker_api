"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class InvitationResponseForm(Form):
    invitation_id = IntegerField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired(), length(min=2, max=64)])
    contact = StringField(validators=[DataRequired()])
