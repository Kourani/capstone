

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Image



def image1_valid(form,field):
    image_1 = form.data['image_1']

    if image_1 and (not image_1.endswith('jpeg') and not image_1.endswith('jpg') and not image_1.endswith('png')):
        raise ValidationError('Image must end with jpeg, jpg, or png')

def image2_valid(form,field):
    image_2 = form.data['image_2']

    if image_2 and (not image_2.endswith('jpeg') and not image_2.endswith('jpg') and not image_2.endswith('png')):
        raise ValidationError('Image must end with jpeg, jpg, or png')

def image3_valid(form,field):
    image_3 = form.data['image_3']

    if image_3 and (not image_3.endswith('jpeg') and not image_3.endswith('jpg') and not image_3.endswith('png')):
        raise ValidationError('Image must end with jpeg, jpg, or png')

def image4_valid(form,field):
    image_4 = form.data['image_4']

    if image_4 and (not image_4.endswith('jpeg') and not image_4.endswith('jpg') and not image_4.endswith('png')):
        raise ValidationError('Image must end with jpeg, jpg, or png')

def image5_valid(form,field):
    image_5 = form.data['image_1']

    if image_5 and (not image_5.endswith('jpeg') and not image_5.endswith('jpg') and not image_5.endswith('png')):
        raise ValidationError('Images must end with jpeg, jpg, or png')


class ImageForm(FlaskForm):
    image_1 = StringField('image_1', validators=[image1_valid])
    image_2 = StringField('image_2', validators=[image2_valid])
    image_3 = StringField('image_3', validators=[image3_valid])
    image_4 = StringField('image_4', validators=[image4_valid])
    image_5 = StringField('image_5', validators=[image5_valid])
