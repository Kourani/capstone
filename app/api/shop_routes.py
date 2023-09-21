from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User, Shop, Product, db
from app.forms import ProductForm, ShopForm
from .auth_routes import validation_errors_to_error_messages



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

@shop_routes.route('/', methods=['POST'])
def new_shop():
    """
    create a new shop

    """

    form = ShopForm()

    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        shop = Shop(
            address=form.data['address'],
            city=form.data['city'],
            state=form.data['state'],
            country=form.data['country']
        )
        db.session.add(shop)
        db.session.commit()
        return shop.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@shop_routes.route('/<int:id>/products', methods=['POST'])
def new_product(id):
    """
    Create a product for a shop based on the shops Id

    """

    form = ProductForm()

    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    shop = Shop.query.get(id)

    if not shop:
        return {'error':'Shop not found'}

    if form.validate_on_submit():
        product = Product(
            shop_id=id,
            price=form.data['price'],
            name=form.data['name'],
            description=form.data['description']
        )
        db.session.add(product)
        db.session.commit()
        return product.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
