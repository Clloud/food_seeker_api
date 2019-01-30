"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired
from app.validators.base import BaseForm as Form


class CommentForm(Form):
    user_id = IntegerField(validators=[DataRequired()])
    restaurant_id = IntegerField(validators=[DataRequired()])
    grade = FloatField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])
