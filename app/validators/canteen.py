"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm as Form


class CanteenPostForm(Form):
    name = StringField(validators=[DataRequired(), length(min=2, max=32)])
    introduction = StringField()
    location = StringField(validators=[DataRequired(), length(min=5, max=50)])
    campus_id = IntegerField(validators=[DataRequired()])


class CanteenPutForm(Form):
    name = StringField()
    introduction = StringField()
    location = StringField()
    campus_id = IntegerField()
    comment_amount = IntegerField()
    grade = FloatField()
    status = IntegerField()
