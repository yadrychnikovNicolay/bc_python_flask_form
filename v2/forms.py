from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, RadioField, SelectField, EmailField, HiddenField)
from wtforms.validators import InputRequired, Length, Email

class MessageForm(FlaskForm):
    subject = SelectField('Subject',choices=['Other', 'Order', 'Repair'])
    fullname = StringField('Full Name', validators=[InputRequired(), Length(max=30)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[InputRequired()])
    country = SelectField('Country', choices=['Narnia', 'London', 'Europe', 'Bad Neighborhood'], validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=10, max=300)])