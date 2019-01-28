"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp
from app.validators.base import BaseForm as Form


class RestaurantForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField()
    canteen_id = IntegerField(validators=[DataRequired()])