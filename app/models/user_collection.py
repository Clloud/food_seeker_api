"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship
from app.models.base import Base


class UserCollection(Base):
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant = relationship('Restaurant')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['restaurant']

