"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, Text, ForeignKey, String, orm
from app.models.base import Base, db


class InvitationResponse(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(Text)
    contact = Column(String(32))
    invitation_id = Column(Integer, ForeignKey("invitation.id"))
    response_status = Column(Integer)

    @staticmethod
    def create_invitation_response(form, user_id):
        with db.auto_commit():
            invitation_response = InvitationResponse()
            invitation_response.set_attrs(form)
            invitation_response.user_id = user_id
            db.session.add(invitation_response)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user_id',  'content', 'contact', 'invitation_id', 'response_status']
