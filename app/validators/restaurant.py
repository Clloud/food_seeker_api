"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, length, Regexp
from app.validators.base import BaseForm as Form


class RestaurantCreateForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField(validators=[length(max=200)])
    canteen_id = IntegerField(validators=[DataRequired()])
    image_amount = IntegerField()


class RestaurantUpdateForm(Form):
    name = StringField(validators=[length(min=2, max=32)])
    introduction = StringField(validators=[length(max=200)])
    canteen_id = IntegerField()
