"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, orm


class Banner(Base):
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey("image.id"))
    image = relationship('Image')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['image']
