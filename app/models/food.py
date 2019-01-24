"""
Enjoy The Code!
"""
#__Auther__:__blank__

from sqlalchemy import Column, Integer, String, Float,SmallInteger, orm
from app.models.base import Base, db
from app.libs.error_code import NotFound


class Cuisine(Base):
    __tablename__='cuisine'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(500), default="暂无")
    price = Column(Float(5), nullable=False)
    grade = Column(Float(5), default=0)
    window_id = Column(Integer, nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Food %r>' % self.id
