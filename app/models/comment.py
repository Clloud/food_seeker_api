"""
Enjoy The Code!
"""
#__Auther__:__blank__

from sqlalchemy import Column, Integer, Float, Text, orm, ForeignKey
from app.models.base import Base


class Comment(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    grade = Column(Float(5), default=0)
    content = Column(Text)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'user_id', 'restaurant_id', 'grade', 'content']
