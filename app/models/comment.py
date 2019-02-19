"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, Float, Text, orm, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.comment_image import CommentImage
from app.models.image import Image


class Comment(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    grade = Column(Float(5), default=0)
    content = Column(Text)
    user = relationship('User', backref='comment')
    restaurant = relationship('Restaurant', backref='comment')
    _images = relationship('CommentImage', backref='comment')
    image_amount = Column(Integer, nullable=False, default=0)

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
    def save_comment(form):
        try:
            image_amount = form.image_amount.data
            with db.auto_commit():
                comment = Comment()
                comment.set_attrs(form)
                comment.image_amount = image_amount
                db.session.add(comment)
            for i in range(image_amount):
                image = request.files.get('image' + str(i + 1))
                result = Image.save_image(image)
                image_id = result["image_id"]
                comment_image = CommentImage()
                comment_image.comment_id = comment.id
                comment_image.image_id = image_id
                db.session.add(comment_image)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
