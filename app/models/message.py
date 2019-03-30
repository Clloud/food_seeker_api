"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, Text, ForeignKey, String, orm
from app.models.base import Base, db


class Message(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(Text)
    is_read = Column(Integer, default=0)
    type = Column(Integer)

    @staticmethod
    def create_message(user_id, type):
        with db.auto_commit():
            message = Message()
            message.user_id = user_id
            message.type = type
            db.session.add(message)

    @staticmethod
    def change_state_of_message(message):
        with db.auto_commit():
            message.is_read = 1
            db.session.add(message)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user_id', 'content', 'is_read', 'type']
