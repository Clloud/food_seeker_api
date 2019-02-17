"""
Enjoy The Code!
"""
#__Auther__:__blank__
from app.validators.base import BaseForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired
from app.libs.error_code import SearchSortError, SearchOrderError


def validate_allow_sort(self, field):
    allow_list = ['best-match', 'grade', 'hot']
    if field.data not in allow_list:
        raise SearchSortError()


def validate_allow_sort_comment(self, field):
    allow_list = ['best-match', 'grade', 'poor', 'image', 'new']
    if field.data not in allow_list:
        raise SearchSortError()


def validate_allow_order(self, field):
    allow_list = ['desc', 'asc']
    if field.data not in allow_list:
        raise SearchOrderError()


class SearchRestaurantForm(Form):
    q = StringField(validators=[DataRequired()])
    sort = StringField(default='best-match', validators=[validate_allow_sort])
    order = StringField(default='desc', validators=[validate_allow_order])


class SearchFoodForm(Form):
    q = StringField(validators=[DataRequired()])
    sort = StringField(default='best-match', validators=[validate_allow_sort])
    order = StringField(default='desc', validators=[validate_allow_order])


class SearchCommentForm(Form):
    q = StringField(validators=[DataRequired()])
    sort = StringField(default='best-match', validators=[validate_allow_sort_comment])
    order = StringField(default='desc', validators=[validate_allow_order])
