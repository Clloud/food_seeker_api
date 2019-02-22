"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class FoodCreateForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField(validators=[length(max=200)])
    price = FloatField(validators=[DataRequired()])
    restaurant_id = IntegerField(validators=[DataRequired()])
    image_amount = IntegerField()


class FoodUpdateForm(Form):
    name = StringField(validators=[length(min=2, max=32)])
    introduction = StringField(validators=[length(max=200)])
    price = FloatField()
    restaurant_id = IntegerField()

