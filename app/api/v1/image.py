"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request, jsonify
from app.models.image import Image
from . import api


@api.route('/image', methods=['POST'])
def create_image():
    image = request.files.get('image')
    result = Image.save_image(image)
    return jsonify(result)
