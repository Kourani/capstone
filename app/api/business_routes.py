from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Business

user_routes = Blueprint('shops', __name__)


@business_routes.route('/')
def businesses():
    """
    Query for all businesses and returns them in a list of business dictionaries
    """
    businesses = Business.query.all()
    return {'businesses': [business.to_dict() for business in businesses]}


@businesses_routes.route('/<int:id>')
def business(id):
    """
    Query for a business by id and returns that business in a dictionary
    """
    business = Business.query.get(id)
    return business.to_dict()
