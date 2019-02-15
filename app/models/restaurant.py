"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.image import Image
from app.models.restaurant_image import RestaurantImage


class Restaurant(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, default=0)
    canteen_id = Column(Integer, ForeignKey("canteen.id"))
    comment_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('RestaurantImage', backref='restaurant')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'grade',
                       'canteen_id', 'comment_amount', 'images', 'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def save_restaurant(form):
        try:
            image_amount = form.image_amount.data
            with db.auto_commit():
                restaurant = Restaurant()
                restaurant.set_attrs(form)
                db.session.add(restaurant)
            for i in range(image_amount):
                image = request.files.get('image' + str(i + 1))
                result = Image.save_image(image)
                image_id = result["image_id"]
                restaurant_image = RestaurantImage()
                restaurant_image.restaurant_id = restaurant.id
                restaurant_image.image_id = image_id
                db.session.add(restaurant_image)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
