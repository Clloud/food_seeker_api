"""
Enjoy The Code!
"""
#__Auther__:__blank__
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.models.canteen import Canteen
from app.libs.error_code import ClientTypeError, ParameterError
from app.validators.base import BaseForm as Form


class CanteenForm(Form):
    name = StringField(validators=[DataRequired(), length(min=5, max=32)])
    location = StringField(validators=[DataRequired(), length(min=5, max=32)])

    def validate_type(self, field):
        try:
            canteen = CanteenForm(field.data)#
        except ValueError as e:
            raise e
