from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField,FileField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('male','Male'),('female','Female')])
    profpic = FileField('Profile Image', validators=[InputRequired()])
    
class ScrapeUrl(FlaskForm):
    url=StringField('URL', validators=[InputRequired()])