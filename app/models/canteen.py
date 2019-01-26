"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float, orm
from app.models.base import Base, db
from app.libs.error_code import NotFound


class Canteen(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, nullable=False, default=0)
    location = Column(String(50), nullable=False)
    campus_id = Column(Integer, nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'introduction', 'grade', 'location', 'comment_amount']

    @staticmethod
    def create_canteen(name, location,campus_id):
        with db.auto_commit():
            canteen = Canteen()
            canteen.name = name
            canteen.location = location
            canteen.campus_id = campus_id
            db.session.add(canteen)


    @staticmethod
    def check_campus_id(campus_id):
        if campus_id != 1 | 2 | 3:
            print(campus_id)
            raise NotFound(message='Illegal campus_id')
        return {"campus_id":campus_id}
