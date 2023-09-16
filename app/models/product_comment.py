from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class ProductComment(db.Model):
    __tablename__ = 'productComments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    item_quality = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default = datetime.now())


    def to_dict(self):
        return {
            'id': self.id,
            'itemQuality' : self.item_quality,
            'comment' : self.comment,
            'createdAt' : self.created_at
        }
