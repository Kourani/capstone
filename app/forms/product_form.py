
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


#product validations
def product_image(form, field):
    image = form.data['image']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_image1(form, field):
    image = form.data['image1']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_image2(form, field):
    image = form.data['image2']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_image3(form, field):
    image = form.data['image3']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_image4(form, field):
    image = form.data['image4']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_image5(form, field):
    image = form.data['image5']

    if not image.endswith('jpeg') and not image.endswith('jpg') and not image.endswith('png'):
        raise ValidationError('Image must end with jpeg, jpg, or png')
        return

def product_price(form, field):
    price = form.data['price']

    if type(price) is not float:
        raise ValidationError('Price must be a number')
        return
    elif price < 0:
        raise ValidationError('Price must be a number greater than or equal to 0')
        return


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=50)])
    price = FloatField('price', validators=[DataRequired('Price must be number')])
    description = StringField('description')
    category = SelectField('Category', choices=[('sweets','Sweets'), ('books','Books'), ('watches', 'Watches'), ('ceramics', 'Ceramics'), ('tools', 'Tools'), ('jewelry', 'Jewelry')])
    image = StringField('image', validators=[product_image])
    image1 = StringField('image1', validators=[product_image1])
    image2 = StringField('image2', validators=[product_image2])
    image3 = StringField('image3', validators=[product_image3])
    image4 = StringField('image4', validators=[product_image4])
    image5 = StringField('image5', validators=[product_image5])
