"""
Enjoy The Code!
"""
#__Auther__:__blank__

from sqlalchemy import Column, Integer, String, Float,SmallInteger, orm
from app.models.base import Base, db
from app.libs.error_code import NotFound


class Comment(db.Model):
    __tablename__='comment'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    window_id = Column(Integer, nullable=False)
    cuisine_id = Column(Integer)
    grade = Column(Float(5), default=0)
    content = Column(String(500))
    create_time = Column(Integer, default=0)
    delete_time = Column(Integer, default=0)

    def __repr__(self):
        return '<Comment %r>' % self.id
