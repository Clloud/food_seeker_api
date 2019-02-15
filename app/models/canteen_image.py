"""
Enjoy The Code!
"""
#__Auther__:__blank__
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship
from app.models.base import Base


class CanteenImage(Base):
    id = Column(Integer, primary_key=True)
    canteen_id = Column(Integer, ForeignKey("canteen.id"))
    image_id = Column(Integer, ForeignKey("image.id"))
    image = relationship('Image')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['image']
