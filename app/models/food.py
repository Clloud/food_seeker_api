"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.food_image import FoodImage
from app.models.image import Image


class Food(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    price = Column(Float(5), nullable=False)
    grade = Column(Float(5), default=0)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    comment_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('FoodImage', backref='food')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'price', 'grade',
                       'restaurant_id', 'comment_amount', 'images', 'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def save_food(form):
        try:
            image_amount = form.image_amount.data
            with db.auto_commit():
                food = Food()
                food.set_attrs(form)
                db.session.add(food)
            for i in range(image_amount):
                image = request.files.get('image' + str(i + 1))
                result = Image.save_image(image)
                image_id = result["image_id"]
                food_image = FoodImage()
                food_image.food_id = food.id
                food_image.image_id = image_id
                db.session.add(food_image)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
