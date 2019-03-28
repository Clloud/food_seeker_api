"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, Text, ForeignKey, String, orm
from app.models.base import Base, db


class InvitationReply(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(Text)
    contact = Column(String(32))
    invitation_id = Column(Integer, ForeignKey("invitation.id"))
    response_status = Column(Integer)

    @staticmethod
    def create_invitation_reply(form, invitation_id, user_id):
        with db.auto_commit():
            invitation_reply = InvitationReply()
            invitation_reply.set_attrs(form)
            invitation_reply.invitation_id = invitation_id
            invitation_reply.user_id = user_id
            db.session.add(invitation_reply)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'user_id',  'content', 'contact', 'invitation_id', 'response_status']
