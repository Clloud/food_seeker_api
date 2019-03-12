from flask import request, jsonify
from app.models.image import Image
from . import api

@api.route('/image', methods=['POST'])
def upload_image():
    image = request.files.get('image')
    return jsonify(Image.save_image(image))
