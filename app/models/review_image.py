# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/2/11 14:55
'''
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship
from app.models.base import Base


class ReviewImage(Base):
    id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey("review.id"))
    image_id = Column(Integer, ForeignKey("image.id"))
    image = relationship('Image')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['image']
