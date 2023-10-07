from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Image (db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('products.id')), nullable=False)

    image_1 = db.Column(db.String)
    image_2 = db.Column(db.String)
    image_3 = db.Column(db.String)
    image_4 = db.Column(db.String)
    image_5 = db.Column(db.String)

    products = db.relationship('Product', back_populates='images')

    def to_dict(self):
        return {
            'id' : self.id,
            'productId' : self.product_id,
            'image1': self.image_1,
            'image2' : self.image_2,
            'image3' : self.image_3,
            'image4' : self.image_4,
            'image5' : self.image_5,
        }
