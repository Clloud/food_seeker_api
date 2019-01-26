"""
Enjoy The Code!
"""
#__Auther__:__blank__
from app.models.canteen import Canteen
from app.validators.canteen import CanteenForm
from app.libs.error_code import Success
from . import api

@api.route('/canteen', methods=['POST'])
def create_canteen():
    form = CanteenForm().validate_for_api()
    Canteen.create_canteen(form.name.data, form.location.data)
    return Success()
