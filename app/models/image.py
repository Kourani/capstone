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
        add_prefix_for_prod('products.id')))

    shop_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('shops.id')
    ))

    category = db.Column(db.String)
    
    image1 = db.Column(db.String)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    image4 = db.Column(db.String)
    image5 = db.Column(db.String)
    image6 = db.Column(db.String)
    image7 = db.Column(db.String)
    image8 = db.Column(db.String)
    image9 = db.Column(db.String)
    image10 = db.Column(db.String)


    products = db.relationship('Product', back_populates='images')
    shops = db.relationship('Shop', back_populates='images')

    def to_dict(self):
        return {
            'id' : self.id,
            'productId' : self.product_id,
            'shopId' : self.shop_id,
            'image1': self.image1,
            'image2' : self.image2,
            'image3' : self.image3,
            'image4' : self.image4,
            'image5' : self.image5,
            'image6' : self.image6,
            'image7' : self.image7,
            'image8' : self.image8,
            'image9' : self.image9,
            'image10' : self.image10
        }
