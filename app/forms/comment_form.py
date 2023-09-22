
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Comment


class ProductForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    item_quality = IntegerField('item_quality', validators=[DataRequired()])

