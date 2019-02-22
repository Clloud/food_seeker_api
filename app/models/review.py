"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, Float, Text, orm, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.review_image import ReviewImage
from app.models.image import Image
from app.models.restaurant import Restaurant


class Review(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    grade = Column(Float(5), default=0)
    content = Column(Text)
    user = relationship('User', backref='review')
    restaurant = relationship('Restaurant', backref='review')
    image_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('ReviewImage', backref='review')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user', 'restaurant', 'grade', 'content', 'images',
                       'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def create_review(form, user_id):
        with db.auto_commit():
            review = Review()
            review.set_attrs(form)
            review.user_id = user_id
            db.session.add(review)

            image_amount = form.image_amount.data
            for i in range(image_amount):
                image = request.files.get('image-' + str(i + 1))
                image_id = Image.save_image(image)["image_id"]

                review_image = ReviewImage()
                review_image.review_id = review.id
                review_image.image_id = image_id
                db.session.add(review_image)

        # 更新评分和评论总数
        # TODO 应该加入消息队列
        Restaurant.update_grade(form['restaurant_id'].data)

