# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/15 00:01
'''
from datetime import datetime

from flask import request, current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import inspect, Column, Integer, SmallInteger, orm
from contextlib import contextmanager
from wtforms import Form
from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv

    def custom_paginate(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', current_app.config['PER_PAGE'], type=int)
        return self.paginate(page, per_page, error_out=False).items


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    update_time = Column(Integer)
    delete_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        if not self.create_time:
            self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs):
        '''set attributes of the model with Form object or dict'''
        if isinstance(attrs, dict):
            for key, value in attrs.items():
                if hasattr(self, key) and key != 'id' and value:
                    setattr(self, key, value)
        elif isinstance(attrs, Form):
            for key in attrs.__dict__:
                if hasattr(self, key) and key != 'id'and getattr(attrs, key).data:
                    setattr(self, key, getattr(attrs, key).data)

    def delete(self):
        '''soft delete'''
        self.status = 0
        self.delete_time = int(datetime.now().timestamp())

    def keys(self):
        return self.fields

    def hide(self, *keys):
        '''hide specific fields of the model'''
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        '''append specific fields of the model'''
        for key in keys:
            self.fields.append(key)
        return self


# class MixinJSONSerializer:
#     @orm.reconstructor
#     def init_on_load(self):
#         self._fields = []
#         self._include = []
#         self._exclude = []
#
#         self._set_fields()
#         self.__prune_fields()
#
#     def _set_fields(self):
#         pass
#
#     def __prune_fields(self):
#         columns = inspect(self.__class__).columns
#         if not self._fields:
#             all_columns = set(columns.keys())
#             self._fields = list(all_columns - set(self._exclude))
#
#     def hide(self, *args):
#         for key in args:
#             self._fields.remove(key)
#         return self
#
#     def keys(self):
#         return self._fields
#
#     def __getitem__(self, key):
#         return getattr(self, key)
