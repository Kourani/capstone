from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Shop

shop_routes = Blueprint('shops', __name__)


@shop_routes.route('/')
def shops():
    """
    Query for all shops and returns them in a list of shop dictionaries
    """
    shops = Shop.query.all()
    return {'shops': [shop.to_dict() for shop in shops]}


@shop_routes.route('/<int:id>')
def shop(id):
    """
    Query for a shop by id and returns that shop in a dictionary
    """
    shop = Shop.query.get(id)
    return shop.to_dict()
