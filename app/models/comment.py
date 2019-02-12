"""
Enjoy The Code!
"""
#__Auther__:__blank__

from sqlalchemy import Column, Integer, Float, Text, orm, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Comment(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    grade = Column(Float(5), default=0)
    content = Column(Text)
    user = relationship('User', backref='comment')
    restaurant = relationship('Restaurant', backref='comment')
    _images = relationship('CommentImage', backref='comment')

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
