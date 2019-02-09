"""
Enjoy The Code!
"""
#__Auther__:__blank__

from wtforms import IntegerField, StringField
from app.validators.base import BaseForm as Form


class PicturePostForm(Form):
    user_id = IntegerField()
    canteen_id = IntegerField()
    restaurant_id = IntegerField()
    food_id = IntegerField()
    comment_id = IntegerField()


class PicturePutForm(Form):
    status = IntegerField()
    url = StringField()
