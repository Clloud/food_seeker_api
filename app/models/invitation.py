"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, Text, ForeignKey, String
from app.models.base import Base, db


class Invitation(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    time = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    content = Column(Text)
    contact = Column(String(32))
    pay = Column(Integer)
    companion_id = Column(Integer, ForeignKey("user.id"))

    @staticmethod
    def create_invitation(form, user_id):
        with db.auto_commit():
            invitation = Invitation()
            invitation.set_attrs(form)
            invitation.user_id = user_id
            db.session.add(invitation)
