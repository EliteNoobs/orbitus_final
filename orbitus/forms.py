from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from orbitus.models import Main

class Register(FlaskForm):
	FullName = StringField('Full Name', validators=[DataRequired()])
	EMAIL = StringField('E-Mail', validators=[DataRequired(), Email()])
	Proceed = SubmitField('Proceed')
	def validate_EMAIL(self,EMAIL):
		current = Main.query.filter_by(EMAIL=EMAIL.data).first()
		if current:
			raise ValidationError('This E-Mail has already been registered!')


class Username(FlaskForm):
	Username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	Password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
	ConfirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
	SignUp = SubmitField('SignUp')
	def validate_Username(self,Username):
		current = Main.query.filter_by(Username=Username.data).first()
		if current:
			raise ValidationError('This username has already been registered!')
	

class PersonalInfo(FlaskForm):
	Age = IntegerField('Age', validators=[DataRequired(), Length(min=0)])
	SignUp = SubmitField('Finish Registration')


class LogIn(FlaskForm):
	Username = StringField('Username', validators=[DataRequired()])
	Password = PasswordField('Password', validators=[DataRequired()])
	RememberMe = BooleanField('Remember Me')
	login = SubmitField('Log In')