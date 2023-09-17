from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Order, CommentA

commentA_routes = Blueprint('productcomments', __name__)


@commentA_routes.route('/')
def comments():
    """
    Query for all product comments and returns them in a list of product comments dictionaries
    """
    comments = CommentA.query.all()
    return {'comments': [comment.to_dict() for comment in comments]}


@commentA_routes.route('/<int:id>')
def comment(id):
    """
    Query for a comment by id and returns that comment in a dictionary
    """
    comment = CommentA.query.get(id)
    return comment.to_dict()
