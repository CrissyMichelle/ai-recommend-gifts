from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class GiftForm(FlaskForm):
    age = IntegerField(
        'Age',
        validators=[DataRequired(), NumberRange(min=0, max=120)]
    )
    gender = SelectField(
        'Gender',
        choices=[
            ('', 'Select one'),
            ('gender-fluid', 'Fluid'),
            ('female', 'Femme'),
            ('male', 'Masc'),
            ('non-binary', 'Non-Binary')
        ],
        validators=[DataRequired()]
    )
    hobby = TextAreaField(
        'Type in some of their hobbies!',
        validators=[DataRequired(), Length(max=200)]
    )
    budget = SelectField(
        'Budget',
        choices=[
            ('', 'Select one'),
            ('low', 'Thrifty'),
            ('medium', 'Mid'),
            ('high', 'Opulent')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Get Gift Recommendations!')
