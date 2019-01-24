"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float, orm
from app.models.base import Base, db


class Canteen(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, nullable=False, default=0)
    location = Column(String(50), nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'introduction', 'grade', 'location', 'comment_amount']

    @staticmethod
    # TODO 请使用set_attrs()批量设置属性
    def create_canteen(name, location):
        with db.auto_commit():
            canteen = Canteen()
            canteen.name = name
            canteen.location = location
            db.session.add(canteen)
