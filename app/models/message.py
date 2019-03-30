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
    state_of_read = Column(Integer, default=0)
    state_of_content = Column(Integer)

    @staticmethod
    def create_message(user_id, state_of_content):
        with db.auto_commit():
            message = Message()
            message.user_id = user_id
            message.state_of_content = state_of_content
            db.session.add(message)

    @staticmethod
    def change_state_of_message(message):
        with db.auto_commit():
            message.state_of_read = 1
            db.session.add(message)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user_id', 'content', 'state_of_read', 'state_of_content']
