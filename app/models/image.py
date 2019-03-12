"""
Enjoy The Code!
"""
#__Auther__:__blank__
import os
import time
import uuid
from flask import current_app
from sqlalchemy import Column, Integer, orm, VARCHAR
from app.models.base import Base, db
from app.libs.error_code import SizeError, TypeError


class Image(Base):
    id = Column(Integer, primary_key=True)
    _url = Column('url', VARCHAR(50))

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'url']

    @property
    def url(self):
        return current_app.config['IMAGE_URL_PREFIX'] + self._url

    @url.setter
    def url(self, value):
        self._url = value

    @classmethod
    def save_image(cls, image):
        '''
        检验图片大小、类型
        将图片压缩并保存到指定目录
        将图片相对路径保存到数据库
        返回图片完整路径和图片的id
        '''
        cls.validate_image(image)
        directory_name, filename = cls.save_to_file(image)

        img = Image()
        with db.auto_commit():
            img.url = '/' + directory_name + '/' + filename
            db.session.add(img)

        return {
            "image_id": img.id,
            "image_url": img.url
        }

    @classmethod
    def save_to_file(cls, image):
        directory_name = time.strftime('%Y%m%d', time.localtime(time.time()))
        directory_path = current_app.config['IMAGE_DIRECTORY'] + '/' + directory_name
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        filename = cls.generate_filename(image)
        file_path = directory_path + '/' + filename
        image.save(file_path)
        return directory_name, filename

    @staticmethod
    def validate_image(image):
        # TODO 校验图片大小
        # image_size = len(image.read()) / 1024 / 1024 # Unit: MB
        # allowed_size = current_app.config['IMAGE_SIZE']
        # if image_size > allowed_size:
        #     raise SizeError(message="Image excess maximum file size of "
        #                             + str(allowed_size) + "MB")

        # 校验图片扩展名
        filename = image.filename
        if not ('.' in filename and
                filename.rsplit('.', 1)[1].upper() in current_app.config['IMAGE_EXTENSIONS']):
            raise TypeError(message="Image type is not allowed")

        return image

    @staticmethod
    def generate_filename(image):
        return str(uuid.uuid1()).replace('-', '') + '.' + image.filename.rsplit('.', 1)[1]
