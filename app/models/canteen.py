"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, String, Float,SmallInteger, orm
from app.models.base import Base, db
from app.libs.error_code import NotFound


class Canteen(Base):
    __tablename__ = 'canteen'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(500), default="暂无")
    grade = Column(Float, nullable=False, default=0)
    location = Column(String(50), nullable=False)
    comment_amount = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Canteen %r>' % self.id

    @orm.reconstructor
    def __init__(self):#
        self.fields = ['name', 'location']

    @staticmethod
    def create_canteen(name, location):
        with db.auto_commit():
            canteen = Canteen()
            canteen.name = name
            canteen.location = location
            db.session.add(canteen)

    @staticmethod
    def verify_create_canteen(name, location):
        canteen = Canteen.query.filter_by(email=name).first()
        if not canteen:
            raise NotFound(message='Canteen already have')
        return {'name': canteen.name, 'location': canteen.auth}
