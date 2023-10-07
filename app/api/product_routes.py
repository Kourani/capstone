from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Product, Comment, Image
from app.forms import ProductForm, ShopForm, CommentForm, ImageForm
from .auth_routes import validation_errors_to_error_messages


product_routes = Blueprint('products', __name__)

#Get all Products
@product_routes.route('/')
def products():
    """
    Query for all products and returns them in a list of product dictionaries
    """
    products = Product.query.all()
    return {'products': [product.to_dict() for product in products]}

#Get one product by Id
@product_routes.route('/<int:id>')
def product(id):
    """
    Query for a product by id and returns that product in a dictionary
    """

    product = Product.query.get(id)
    return product.to_dict()


#Edit product
@product_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def update_product(id):

    form = ProductForm()

    product = Product.query.get(id)

    form['csrf_token'].data = request.cookies['csrf_token']

    if not product:
        return {'error' : 'Product not found'}

    if form.validate_on_submit():
        product.name = form.data['name']
        product.price = form.data['price']
        product.description = form.data['description']
        product.category = form.data['category']

        db.session.commit()

        return product.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

#delete product
@product_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_product(id):
    # form = ProductForm

    product = Product.query.get(id)

    if not product:
        return {'error':'Product not found'}, 401

    if product:
        db.session.delete(product)
        db.session.commit()

    return {'message':'Successfully deleted'}, 200



#Create a comment for a product based on a products id
@product_routes.route('/<int:id>/comments', methods=['POST'])
@login_required
def new_comment(id):

    form = CommentForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    product = Product.query.get(id)

    if not product:
        return {'error' : 'Product not found'}

    if form.validate_on_submit():
        comment = Comment(
            user_id=current_user.id,
            product_id=id,
            comment = form.data['comment'],
            # item_quality=form.data['item_quality']
        )
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict()

    return {'errors':validation_errors_to_error_messages(form.errors)}, 401

#Create images for a product based on a products id
@product_routes.route('/<int:id>/images', methods=['POST'])
@login_required
def new_image(id):

    form = ImageForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    product = Product.query.get(id)

    if not product:
        return {'errors':'Image not found'}

    if form.validate_on_submit():
        image = Image(
            product_id = id,
            image_1 = form.data['image_1'],
            image_2 = form.data['image_2'],
            image_3 = form.data['image_3'],
            image_4 = form.data['image_4'],
            image_5 = form.data['image_5']
        )
        db.session.add(image)
        db.session.commit()
        return image.to_dict()
    return {'errors':validation_errors_to_error_messages(form.errors)}, 400

#Edit images for a product based on a products id
@product_routes.route('/<int:id>/images', methods=['PUT'])
@login_required
def updated_images(id):

    form = ImageForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    product = Product.query.get(id)

    if not product:
        return {'errors':'Image not found'}

    if form.validate_on_submit():
        image = Image(
            product_id = id,
            image_1 = form.data['image_1'],
            image_2 = form.data['image_2'],
            image_3 = form.data['image_3'],
            image_4 = form.data['image_4'],
            image_5 = form.data['image_5']
        )
        db.session.add(image)
        db.session.commit()
        return image.to_dict()
    return {'errors':validation_errors_to_error_messages(form.errors)}, 400
