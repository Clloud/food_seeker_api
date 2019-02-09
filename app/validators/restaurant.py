"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, length, Regexp
from app.validators.base import BaseForm as Form


class RestaurantPostForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField()
    canteen_id = IntegerField(validators=[DataRequired()])


class RestaurantPutForm(Form):
    name = StringField()
    introduction = StringField()
    grade = FloatField()
    comment_amount = IntegerField()
    status = IntegerField()
    canteen_id = IntegerField()
