from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Product

product_routes = Blueprint('products', __name__)


@product_routes.route('/')
def products():
    """
    Query for all products and returns them in a list of product dictionaries
    """
    products = Product.query.all()
    return {'products': [product.to_dict() for product in products]}


@product_routes.route('/<int:id>')
def product(id):
    """
    Query for a product by id and returns that product in a dictionary
    """
    product = Product.query.get(id)
    return product.to_dict()