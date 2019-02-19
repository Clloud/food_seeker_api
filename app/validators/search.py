"""
Enjoy The Code!
"""
#__Auther__:__blank__
from app.validators.base import BaseForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired
from app.libs.error_code import ParameterError


class BaseSearchForm(Form):
    q = StringField(validators=[DataRequired()])
    order = StringField(default='desc')

    def validate_order(self, field):
        if field.data not in ('desc', 'asc'):
            raise ParameterError(message='Invalid order type')


class SearchRestaurantForm(BaseSearchForm):
    sort = StringField(default='grade')

    def validate_sort(self, field):
        if field.data not in ('grade', 'hot'):
            raise ParameterError(message='Invalid sort type')


class SearchFoodForm(BaseSearchForm):
    sort = StringField(default='best-match')

    def validate_sort(self, field):
        if field.data not in ('grade', 'hot'):
            raise ParameterError(message='Invalid sort type')


class SearchCommentForm(BaseSearchForm):
    sort = StringField(default='best-match')

    def validate_sort(self, field):
        if field.data not in ('grade', 'new', 'image'):
            raise ParameterError(message='Invalid sort type')
