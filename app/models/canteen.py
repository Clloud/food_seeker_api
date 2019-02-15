"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, String, Float, orm
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.canteen_image import CanteenImage
from app.models.image import Image


class Canteen(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, nullable=False, default=0)
    location = Column(String(50), nullable=False)
    campus_id = Column(Integer, nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('CanteenImage', backref='canteen')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'grade',
                       'location', 'campus_id', 'comment_amount', 'images', 'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def save_canteen(form):
        try:
            image_amount = form.image_amount.data
            with db.auto_commit():
                canteen = Canteen()
                canteen.set_attrs(form)
                db.session.add(canteen)
            for i in range(image_amount):
                image = request.files.get('image'+str(i+1))
                result = Image.save_image(image)
                image_id = result["image_id"]
                canteen_image = CanteenImage()
                canteen_image.canteen_id = canteen.id
                canteen_image.image_id = image_id
                db.session.add(canteen_image)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
