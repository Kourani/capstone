
from flask import Blueprint, jsonify
from app.models import ProductComment


productComment_routes = Blueprint('productComments', __name__)

@productComment_routes.route('/')
def productComments():
    """
    Query for all product comments and returns them in a list of productComment dictionaries

    """

    productComments = ProductComment.query.all()
    return {'productComments': [productComment.to_dict() for productComment in productComments]}

@productComment_routes.route('/<int:id>')
def productComment(id):

    """
    Query for a productComment by id and returns that product comment in a dictionary
    """

    productComment = ProductComment.query.get(id)
    return productComment.to_dict()
