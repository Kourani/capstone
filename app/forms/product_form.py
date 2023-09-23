
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    description = StringField('description')
    image = StringField('image')
