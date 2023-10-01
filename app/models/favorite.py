from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)

    category = db.Column(db.String)

    number = db.Column(db.Integer)

    users = db.relationship('User', back_populates='favorites') #user table fill out favorites

    def to_dict(self):
        return {
            'id' : self.id,
            'userId' : self.user_id,
            'category' : self.category,
            'number' : self.number
        }
