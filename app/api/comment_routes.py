from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Order, Comment

comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/')
def comments():
    """
    Query for all comments and returns them in a list of comments dictionaries
    """
    comments = Comment.query.all()
    return {'comments': [comment.to_dict() for comment in comments]}


@comment_routes.route('/<int:id>')
def comment(id):
    """
    Query for a comment by id and returns that comment in a dictionary
    """
    comment = Comment.query.get(id)
    return comment.to_dict()
