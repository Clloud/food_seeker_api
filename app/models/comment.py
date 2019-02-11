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
    images = relationship('CommentImage', backref='comment')
    user = relationship('User', backref='comment')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'user', 'restaurant_id', 'grade', 'content', 'images']
