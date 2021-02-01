from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    firstname = StringField('FirstName', validators=[DataRequired()])
    lastname = StringField('LastName', validators=[DataRequired()])
    middlename = StringField('MiddleName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    mobile = IntegerField('Contact', validators=[DataRequired()])
    alias = StringField('Alias', validators=[DataRequired()])
    submit = SubmitField('Submit')