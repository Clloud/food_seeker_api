"""
Enjoy The Code!
"""
#__Auther__:__blank__
import os
from PIL import Image
from flask import current_app
from sqlalchemy import Column, Integer, orm, ForeignKey, VARCHAR
from app.models.base import Base
import datetime
import random

basedir = os.path.dirname(os.path.dirname(__file__))


class Picture(Base):
    id = Column(Integer, primary_key=True)
    url = Column(VARCHAR(50))
    user_id = Column(Integer, ForeignKey("user.id"))
    canteen_id = Column(Integer, ForeignKey("canteen.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    food_id = Column(Integer, ForeignKey("food.id"))
    comment_id = Column(Integer, ForeignKey("comment.id"))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'url', 'user_id', 'canteen_id', 'restaurant_id', 'food_id', 'comment_id']

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

    def save_picture(self, img):
        path = basedir + "\pictures\\"
        file_path = path + img.filename
        img.save(file_path)
        im = Image.open(file_path)
        im.thumbnail(current_app.config['SIZE'])
        im.save(file_path, "JPEG")

    def create_unique_name(self):
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(0, 99)
        if random_num <= 10:
            random_num = str(0) + str(random_num)
        uniquenum = str(now_time) + str(random_num)
        return uniquenum+".jpg"
