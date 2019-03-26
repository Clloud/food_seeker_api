"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, Text, orm, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, db


class Comment(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    review_id = Column(Integer, ForeignKey("review.id"))
    content = Column(Text)
    user = relationship('User', backref='comment')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user', 'content', 'create_time']

    @staticmethod
    def create_comment(form, user_id):
        with db.auto_commit():
            comment = Comment()
            comment.set_attrs(form)
            comment.user_id = user_id
            db.session.add(comment)
