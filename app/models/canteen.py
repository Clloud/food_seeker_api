"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
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
    campus_id = Column(Integer, ForeignKey("campus.id"))
    review_amount = Column(Integer, nullable=False, default=0)
    image_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('CanteenImage', backref='canteen')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'grade',
                       'location', 'campus_id', 'review_amount', 'image_amount', 'images', 'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def create_canteen(form):
        # TODO 验证表单中图片的key，或修改图片上传方式
        with db.auto_commit():
            canteen = Canteen()
            canteen.set_attrs(form)
            db.session.add(canteen)

            image_amount = form.image_amount.data
            for i in range(image_amount):
                image = request.files.get('image-' + str(i + 1))
                image_id = Image.save_image(image)["image_id"]

                canteen_image = CanteenImage()
                canteen_image.canteen_id = canteen.id
                canteen_image.image_id = image_id
                db.session.add(canteen_image)

    @classmethod
    def update_grade(cls, canteen_id):
        from app.models.restaurant import Restaurant

        # calculate review amount and average grade
        restaurants = Restaurant.query.filter_by(canteen_id=canteen_id).all()
        amount = sum([r.review_amount for r in restaurants])
        grade = sum([r.grade * r.review_amount for r in restaurants]) / amount

        with db.auto_commit():
            canteen = cls.query.filter_by(id=canteen_id).first_or_404()
            canteen.review_amount = amount
            canteen.grade = grade
            db.session.add(canteen)

