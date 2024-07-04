from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

class LookUpForm(FlaskForm):
    number = StringField('Phone Number', validators=[DataRequired()])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField('Birth Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[validators.DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    firstName = StringField('First Name')
    submit = SubmitField('Submit')
