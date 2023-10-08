
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


#product validations
def product_image(form, field):
    image = form.data['image']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')

def product_price(form, field):
    price = form.data['price']

    if type(price) is not float:
        raise ValidationError('Price must be a number')
        return


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired('Price must be number')])
    description = StringField('description')

    category = SelectField('Category', choices=[('sweets','Sweets'), ('books','Books'), ('watches', 'Watches'), ('ceramics', 'Ceramics'), ('tools', 'Tools'), ('jewelry', 'Jewelry')])
    image = StringField('image', validators=[product_image])

#options = [('toys','Toys'), 'books']
