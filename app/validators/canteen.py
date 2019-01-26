"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp
from app.validators.base import BaseForm as Form


class CanteenForm(Form):
    name = StringField(validators=[DataRequired(), length(min=5, max=32)])
    location = StringField(validators=[DataRequired(), length(min=5, max=32)])
    campus_id = IntegerField(validators=[DataRequired()])
