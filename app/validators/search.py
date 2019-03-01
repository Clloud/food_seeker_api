"""
Enjoy The Code!
"""
#__Auther__:__blank__
from app.validators.base import BaseForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired, AnyOf


class BaseSearchForm(Form):
    q = StringField(validators=[DataRequired()])
    order = StringField(validators=[AnyOf('desc', 'asc')],
                        default='desc')


class SearchRestaurantForm(BaseSearchForm):
    sort = StringField(validators=[AnyOf('grade', 'hot')],
           default='grade')


class SearchFoodForm(BaseSearchForm):
    sort = StringField(validators=[AnyOf('grade', 'hot')],
           default='best-match')


class SearchReviewForm(BaseSearchForm):
    sort = StringField(validators=[AnyOf('grade', 'hot', 'best-match')],
                       default='best-match')


class SearchUserForm(BaseSearchForm):
    sort = StringField(validators=[AnyOf('email', 'mobile')], default='mobile')
