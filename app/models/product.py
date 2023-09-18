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
    owner_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')))

    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)

    shops = db.relationship('Shop', back_populates='products') #shop table fill out products

    def to_dict(self):
        return {
            'id' : self.id,
            'ownerId': self.owner_id,
            'shopId' : self.shop_id,
            'name' : self.name,
            'category' : self.category,
            'description' : self.description,
            'price' : self.price,

        }
