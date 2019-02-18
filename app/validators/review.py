"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired
from app.validators.base import BaseForm as Form


class CommentCreateForm(Form):
    user_id = IntegerField(validators=[DataRequired()])
    restaurant_id = IntegerField(validators=[DataRequired()])
    grade = FloatField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])
    image_amount = IntegerField(validators=[DataRequired()])


class CommentUpdateForm(Form):
    user_id = IntegerField()
    restaurant_id = IntegerField()
    grade = FloatField()
    content = StringField()
    status = IntegerField()
