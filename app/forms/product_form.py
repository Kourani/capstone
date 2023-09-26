
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


#product validations
def product_image(form, field):
    image = form.data['image']

    if not image.endswith('jpeg') or image.endswith('jpg'):
        raise ValidationError('Image must end with jpeg or jpg')

def product_price(form, field):
    price = form.data['price']

    if type(price) is not float:
        raise ValidationError('Price must be a number')


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired(message = product_price)])
    description = StringField('description')
    category = StringField('category')
    image = StringField('image', validators=[product_image])
