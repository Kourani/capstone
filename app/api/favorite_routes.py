from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Favorite
from app.forms import CommentForm
from .auth_routes import validation_errors_to_error_messages

favorite_routes = Blueprint('favorites', __name__)


#get all favorites
@favorite_routes.route('/')
def favorites():
    favorites = Favorite.query.all()
    return {'favorites': [favorite.to_dict() for favorite in favorites]}

#get favorite by Id
@favorite_routes.route('/<int:id>')
def favorite(id):
    favorite = Favorite.query.get(id)
    return favorite.to_dict()
