"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship
from app.models.base import Base, db


class UserFollow(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    following_id = Column(Integer, ForeignKey("user.id"))

    @staticmethod
    def create_follow(user_id, following_id):
        user_follow = UserFollow.query.filter(
            UserFollow.user_id == user_id, UserFollow.following_id == following_id).first()
        with db.auto_commit():
            if not user_follow:
                user_follow = UserFollow()
                user_follow.user_id = user_id
                user_follow.following_id = following_id
            else:
                user_follow.status = 1
            db.session.add(user_follow)

    @staticmethod
    def delete_follow(user_id, following_id):
        with db.auto_commit():
            user_follow = UserFollow.query.filter_by(
                user_id=user_id, following_id=following_id).first_or_404()
            user_follow.delete()
