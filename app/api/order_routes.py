from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Order

order_routes = Blueprint('orders', __name__)


@order_routes.route('/')
def orders():
    """
    Query for all products and returns them in a list of order dictionaries
    """
    orders = Order.query.all()
    return {'orders': [order.to_dict() for order in orders]}


@order_routes.route('/<int:id>')
def order(id):
    """
    Query for a order by id and returns that order in a dictionary
    """
    order = Order.query.get(id)
    return order.to_dict()
