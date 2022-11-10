from re import L
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField # imports our fields that we will use in the form
from wtforms.validators import DataRequired, Length, Email

## Class for the contact form ##
class ContactMeForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=40)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=5, max=300)])
    submit = SubmitField('Submit')


