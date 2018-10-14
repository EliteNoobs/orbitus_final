from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Register(FlaskForm):
	name = StringField('Full Name', validators=[DataRequired()])
	email = StringField('E-Mail', validators=[DataRequired(), Email()])
	proceed = SubmitField('Proceed')

class LogIn(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
	remember = BooleanField('Remember Me')
	login = SubmitField('Log In')

class Username(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
	confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
	signup = SubmitField('SignUp')
	
class PersonalInfo(FlaskForm):
	age = IntegerField('Age', validators=[DataRequired(), Length(min=0)])
	signup = SubmitField('Finish Registration')