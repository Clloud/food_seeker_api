"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class CanteenForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField()
    location = StringField(validators=[DataRequired(), length(min=5, max=50)])
    campus_id = IntegerField(validators=[DataRequired()])
