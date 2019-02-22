# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/2/22 17:59
'''
from app.models.base import Base
from sqlalchemy import Column, Integer, String, orm


class Campus(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name']
