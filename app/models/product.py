from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    business_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('businesses.id')))
    owner_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')))
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)

    businesses = db.relationship('Business', back_populates='products') #business table fill out products

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'category' : self.category,
            'price' : self.price,
            'ownerId': self.owner_id,
            'businessId' : self.business_id
        }
