from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
# from sqlalchemy.dialects.mysql import DECIMAL


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    # price = db.Column(DECIMAL(precision=10, scale=2))

    # users = db.relationship('User', back_populates='products')

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'category' : self.category,
            'price' : self.price
        }
