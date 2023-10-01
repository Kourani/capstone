from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Order, Comment, Shop, Product
from app.forms import CommentForm
from .auth_routes import validation_errors_to_error_messages

comment_routes = Blueprint('comments', __name__)


#get all comments
@comment_routes.route('/')
def comments():
    comments = Comment.query.all()
    return {'comments': [comment.to_dict() for comment in comments]}

#get comment by Id
@comment_routes.route('/<int:id>')
def comment(id):
    comment = Comment.query.get(id)
    return comment.to_dict()

#edit comment
@comment_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_comment(id):
    form = CommentForm()

    comment = Comment.query.get(id)

    form['csrf_token'].data = request.cookies['csrf_token']

    if not comment:
        return {'error': 'Comment not found'}

    if form.validate_on_submit():
        comment.comment=form.data['comment']

        db.session.commit()

        return comment.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@comment_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_comment(id):

    form = CommentForm()

    comment = Comment.query.get(id)

    form['csrf_token'].data = request.cookies['csrf_token']

    if not comment:
        return {'error': 'Comment not found'}

    if comment:
        db.session.delete(comment)
        db.session.commit()

    return {'message':'Successfully Deleted'}, 200
