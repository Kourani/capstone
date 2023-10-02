from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Image
from .auth_routes import validation_errors_to_error_messages

image_routes = Blueprint('images', __name__)


#get all product images
@image_routes.route('/')
def images():
    images = Image.query.all()
    return {'images': [image.to_dict() for image in images]}

#get product image by id
@image_routes.route('/<int:id>')
def image(id):
    image = Image.query.get(id)
    return image.to_dict()
