from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired("Pleae Enter Valid Username"), validators.Length(min=5, max=10, message="Invalid Length")])
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=5, max=10, message="Invalid Length")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired("Please Enter Name"), validators.Length(min=3, max=50, message="Invalid Length")])
    phoneNumber = StringField('Phone Number', validators=[validators.DataRequired("Please Enter Valid Phone Number"), validators.Length(min=7, max=10, message="Invalid Length Phone Number")])
    description = TextAreaField('Description', validators=[validators.DataRequired("Please Enter Valid Description"), validators.Length(min=10, max=200, message="Invalid Length Description")])
    submit = SubmitField('Submit')
