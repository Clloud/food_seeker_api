"""
Enjoy The Code!
"""
#__Auther__:__blank__

from wtforms import IntegerField
from app.validators.base import BaseForm as Form


class PictureForm(Form):
    user_id = IntegerField()
    canteen_id = IntegerField()
    restaurant_id = IntegerField()
    food_id = IntegerField()
    comment_id = IntegerField()
