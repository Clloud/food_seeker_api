"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship
from app.models.base import Base, db


class UserCollection(Base):
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant = relationship('Restaurant')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['restaurant']

    @staticmethod
    def create_collection(uid, restaurant_id):
        with db.auto_commit():
            user_collection = UserCollection()
            user_collection.user_id = uid
            user_collection.restaurant_id = restaurant_id
            db.session.add(user_collection)

    @staticmethod
    def delete_collection(uid, restaurant_id):
        with db.auto_commit():
            user_collection = UserCollection().query.filter_by(
                user_id=uid, restaurant_id=restaurant_id).first_or_404()
            user_collection.delete()
