from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Shop, Product
from app.forms import ProductForm, ShopForm
from .auth_routes import validation_errors_to_error_messages



shop_routes = Blueprint('shops', __name__)

#create a product for a shop
@shop_routes.route('/<int:id>/products', methods=['POST'])
@login_required
def new_product(id):

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

#create a shop
@shop_routes.route('/', methods=['POST'])
@login_required
def new_shop():

    form = ShopForm()

    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    print(current_user,'!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    if form.validate_on_submit():
        shop = Shop(
            owner_id=current_user.id,
            address=form.data['address'],
            city=form.data['city'],
            state=form.data['state'],
            country=form.data['country'],
            name=form.data['name'],
            currency=form.data['currency']
        )
        db.session.add(shop)
        db.session.commit()
        return shop.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

#edit a shop
@shop_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def update_shop(id):

    form=ShopForm()
    shop = Shop.query.get(id)
    # # Get the csrf_token from the request cookie and put it into the
    # # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    if shop:
        shop.owner_id=current_user.id
        shop.address=form.data['address']
        shop.city=form.data['city']
        shop.state=form.data['state']
        shop.country=form.data['country']
        shop.name=form.data['name']
        shop.currency=form.data['currency']

        db.session.commit()

        return shop.to_dict()

    return {'errors': validation_errors_to_error_messages(errors)}, 401

#get all shops
@shop_routes.route('/')
def shops():

    shops = Shop.query.all()
    return {'shops': [shop.to_dict() for shop in shops]}


#get shop by id
@shop_routes.route('/<int:id>')
def shop(id):

    shop = Shop.query.get(id)
    return shop.to_dict()
