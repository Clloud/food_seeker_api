"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class InvitationForm(Form):
    time = IntegerField(validators=[DataRequired()])
    restaurant_id = IntegerField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired(), length(min=2, max=64)])
    contact = StringField(validators=[DataRequired()])
    pay = IntegerField(validators=[DataRequired()])
