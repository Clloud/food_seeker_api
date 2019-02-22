"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange
from app.validators.base import BaseForm as Form


class BaseReviewForm(Form):
    restaurant_id = IntegerField(validators=[DataRequired()])
    grade = FloatField(validators=[NumberRange(min=0, max=5)])
    content = StringField(validators=[DataRequired()])


class ReviewCreateForm(BaseReviewForm):
    image_amount = IntegerField()


class ReviewUpdateForm(BaseReviewForm):
    pass
