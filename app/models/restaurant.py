"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
from app.models.base import Base, db


class Restaurant(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, default=0)
    canteen_id = Column(Integer, ForeignKey("restaurant.id"))
    comment_amount = Column(Integer, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'introduction', 'grade', 'canteen_id', 'comment_amount']


    @staticmethod
    def create_Restaurant(name, introduction, canteen_id):
        # TODO 函数参数需要重新设计
        with db.auto_commit():
            restaurant = Restaurant()
            restaurant.name = name
            restaurant.introduction = introduction
            restaurant.canteen_id = canteen_id
            db.session.add(restaurant)