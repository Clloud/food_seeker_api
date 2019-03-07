"""
Enjoy The Code!
"""
#__Auther__:__blank__
from app.libs.error_code import ParameterError
from app.validators.base import BaseForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired, AnyOf


class BaseSearchForm(Form):
    q = StringField(validators=[DataRequired()])
    order = StringField(validators=[AnyOf(['desc', 'asc'])], default='desc')


class SearchRestaurantForm(BaseSearchForm):
    sort = StringField()

    def validate_sort(self, field):
        if not field.data:
            field.data = 'grade'
        if field.data not in ['grade', 'hot']:
            raise ParameterError(message='Invalid value, must be one of: hot, grade.')


class SearchFoodForm(BaseSearchForm):
    sort = StringField()

    def validate_sort(self, field):
        if not field.data:
            field.data = 'grade'
        if field.data not in ['grade', 'hot']:
            raise ParameterError(message='Invalid value, must be one of: hot, grade.')


class SearchReviewForm(BaseSearchForm):
    sort = StringField()

    def validate_sort(self, field):
        if not field.data:
            field.data = 'grade'
        if field.data not in ['grade', 'hot']:
            raise ParameterError(message='Invalid value, must be one of: hot, grade, best-match.')


class SearchUserForm(BaseSearchForm):
    sort = StringField()

    def validate_sort(self, field):
        if not field.data:
            field.data = 'new'
        if field.data not in ['new']:
            raise ParameterError(message='Invalid value, must be one of:new.')
