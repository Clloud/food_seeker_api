"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange
from app.validators.base import BaseForm as Form


class CommentForm(Form):
    review_id = IntegerField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])