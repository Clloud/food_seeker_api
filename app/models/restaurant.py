"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float,SmallInteger, orm
from app.models.base import Base, db
from app.libs.error_code import NotFound


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(500), default="暂无")
    grade = Column(Float, default=0)
    canteen_id = Column(Integer)
    comment_amount = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Restaurant %r>' % self.id
