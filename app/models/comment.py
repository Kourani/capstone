from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('products.id')), nullable=True)

    item_quality = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default = datetime.now())

    users = db.relationship('User', back_populates= 'comments')
    products =db.relationship('Product', back_populates='comments')

    def to_dict(self):
        return {
            'id':self.id,
            'userId':self.user_id,
            'productId':self.product_id,
            'itemQuality':self.item_quality,
            'comment':self.comment,
            'createdAt':self.created_at
        }
