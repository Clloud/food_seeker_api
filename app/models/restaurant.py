"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import request
from sqlalchemy import Column, Integer, String, Float, orm, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.image import Image
from app.models.restaurant_image import RestaurantImage


class Restaurant(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    introduction = Column(String(200), default="")
    grade = Column(Float, default=0)
    canteen_id = Column(Integer, ForeignKey("canteen.id"))
    review_amount = Column(Integer, nullable=False, default=0)
    _images = relationship('RestaurantImage', backref='restaurant')

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name', 'introduction', 'grade',
                       'canteen_id', 'review_amount', 'images', 'create_time']

    @property
    def images(self):
        return [item.image for item in self._images]

    @images.setter
    def images(self, value):
        self._images = value

    @staticmethod
    def create_restaurant(form):
        with db.auto_commit():
            restaurant = Restaurant()
            restaurant.set_attrs(form)
            db.session.add(restaurant)

            image_amount = form.image_amount.data
            for i in range(image_amount):
                image = request.files.get('image-' + str(i + 1))
                image_id = Image.save_image(image)["image_id"]

                restaurant_image = RestaurantImage()
                restaurant_image.restaurant_id = restaurant.id
                restaurant_image.image_id = image_id
                db.session.add(restaurant_image)

    @classmethod
    def update_grade(cls, restaurant_id):
        from app.models.review import Review
        from app.models.canteen import Canteen

        # calculate review amount and average grade
        reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
        review_grades = [review.grade for review in reviews]
        amount = len(review_grades)
        grade = sum(review_grades) / amount

        with db.auto_commit():
            restaurant = cls.query.filter_by(id=restaurant_id).first_or_404()
            restaurant.review_amount = amount
            restaurant.grade = grade
            db.session.add(restaurant)

        # Update corresponding canteen's grade
        if restaurant.canteen_id:
            Canteen.update_grade(restaurant.canteen_id)