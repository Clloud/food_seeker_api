"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class FoodForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField()
    price = FloatField(validators=[DataRequired()])
    restaurant_id = IntegerField(validators=[DataRequired()])
