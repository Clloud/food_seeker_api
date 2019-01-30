"""
Enjoy The Code!
"""
#__Auther__:__blank__

from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
from app.models.base import Base


class Food(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    price = Column(Float(5), nullable=False)
    grade = Column(Float(5), default=0)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    comment_amount = Column(Integer, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'introduction', 'price', 'grade', 'restaurant_id', 'comment_amount']
