"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class InvitationReplyForm(Form):
    content = StringField(validators=[DataRequired(), length(min=2, max=64)])
    contact = StringField(validators=[DataRequired()])
