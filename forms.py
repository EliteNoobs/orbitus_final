from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Register(FlaskForm):
	FullName = StringField('Full Name', validators=[DataRequired()])
	EMAIL = StringField('E-Mail', validators=[DataRequired(), Email()])
	Proceed = SubmitField('Proceed')

class LogIn(FlaskForm):
	Username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	Password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=63)])
	RememberMe = BooleanField('Remember Me')
	login = SubmitField('Log In')

class Username(FlaskForm):
	Username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	Password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=63)])
	ConfirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
	SignUp = SubmitField('SignUp')
	
class PersonalInfo(FlaskForm):
	Age = IntegerField('Age', validators=[DataRequired(), Length(min=0)])
	SignUp = SubmitField('Finish Registration')