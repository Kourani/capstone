from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Favorite
from app.forms import FavoriteForm
from .auth_routes import validation_errors_to_error_messages

favorite_routes = Blueprint('favorites', __name__)


#get only current users favorites
@favorite_routes.route('/')
@login_required
def favorites():
    # favorites = Favorite.query.all()
    favorites = Favorite.query.filter(Favorite.user_id == current_user.id).all()
    # print(favorites, 'favoritesssss')
    return {'favorites': [favorite.to_dict() for favorite in favorites]}

#get favorite by Id
@favorite_routes.route('/<int:id>')
@login_required
def favorite(id):
    favorite = Favorite.query.get(id)
    return favorite.to_dict()

#add favorite
@favorite_routes.route('/', methods=['POST'])
@login_required
def new_favorite():

    form = FavoriteForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        favorite = Favorite(
        user_id = current_user.id,
        category = form.data['category'],
        number = form.data['number']
        )

        db.session.add(favorite)
        db.session.commit()

        return favorite.to_dict()

    return {'errors':validation_errors_to_error_messages(form.errors)}, 401

#delete favorite
@favorite_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_favorite(id):

    favorite = Favorite.query.get(id)

    if not favorite:
        return {'error': 'Favorite not found'}

    if favorite:
        db.session.delete(favorite)
        db.session.commit()

    return {'message':'Successfully deleted'}, 200
