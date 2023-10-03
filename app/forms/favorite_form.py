


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Favorite

class FavoriteForm(FlaskForm):
    number = IntegerField('name', validators=[DataRequired()])
    category = StringField('price', validators=[DataRequired()])
