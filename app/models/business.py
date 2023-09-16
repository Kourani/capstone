from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Business(db.Model):
    __tablename__ = 'businesses'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    language = db.Column(db.String)
    currency = db.Column(db.String)
    created_at = db.Column(db.DateTime, default = datetime.now())

    # users = db.relationship('User', back_populates='businesses')

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'state' : self.state,
            'country' : self.country,
            'language' : self.language,
            'createdAt' : self.created_at
        }
