from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    shop_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('shops.id')))

    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    image = db.Column(db.String)
    image1 = db.Column(db.String)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    image4 = db.Column(db.String)
    image5 = db.Column(db.String)

    shops = db.relationship('Shop', back_populates='products')
    comments = db.relationship('Comment', back_populates='products')
    images = db.relationship('Image', back_populates='products', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id' : self.id,
            'shopId' : self.shop_id,
            'name' : self.name,
            'category' : self.category,
            'description' : self.description,
            'price' : self.price,
            'image' : self.image,
            'image1' : self.image1,
            'image2' : self.image2,
            'image3' : self.image3,
            'image4' : self.image4,
            'image5' : self.image5
        }
