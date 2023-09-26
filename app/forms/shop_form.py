
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, ValidationError
from app.models import Shop


def shop_image(form, field):
    image = form.data['image']
    if not image.endswith('jpeg') or image.endswith('jpg'):
        raise ValidationError('Image must end with jpeg or jpg')

class ShopForm(FlaskForm):
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    name = StringField('name')
    currency = StringField('currency')
    image = StringField('image', validators=[shop_image])
