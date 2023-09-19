from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Shop(db.Model):
    __tablename__ = 'shops'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)

    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    currency = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.now())

    users = db.relationship('User', back_populates='shops') #user table fill out business
    products = db.relationship('Product', back_populates='shops') #product table fill out business


    def to_dict(self):
        return {
            'id':self.id,
            'ownerId':self.owner_id,
            'address':self.address,
            'city':self.city,
            'state':self.state,
            'country':self.country,
            'name':self.name,
            'currency':self.currency,
            'createdAt':self.created_at
        }
