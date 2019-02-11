"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float, orm
from app.models.base import Base


class Canteen(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, nullable=False, default=0)
    location = Column(String(50), nullable=False)
    campus_id = Column(Integer, nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'grade',
                       'location', 'campus_id', 'comment_amount']


