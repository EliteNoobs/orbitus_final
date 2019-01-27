from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from orbitus.models import User, EventModel
from datetime import datetime


class Register(FlaskForm):
	FullName = StringField('Full Name', validators=[DataRequired()])
	EMAIL = StringField('E-Mail', validators=[DataRequired(), Email()])
	Proceed = SubmitField('Proceed')
	def validate_EMAIL(self,EMAIL):
		current = User.query.filter_by(EMAIL=EMAIL.data).first()
		if current:
			raise ValidationError('This E-Mail has already been registered!')


class Username(FlaskForm):
	Username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	Password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
	ConfirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
	SignUp = SubmitField('SignUp')
	def validate_Username(self,Username):
		current = User.query.filter_by(Username=Username.data).first()
		if current:
			raise ValidationError('This username has already been registered!')


class LogIn(FlaskForm):
	Username = StringField('Username', validators=[DataRequired()])
	Password = PasswordField('Password', validators=[DataRequired()])
	RememberMe = BooleanField('Remember Me')
	login = SubmitField('Log In')
	
class GroupForm(FlaskForm):
	GroupName = StringField('Name', validators=[DataRequired(), Length(min=8)])
	Description = TextAreaField('Description', validators=[DataRequired(), Length(min=0)])
	creategroupbtn = SubmitField('Create your Group')
	def validate_Group(self,GroupName):
		current = GroupModel.query.filter_by(groupname=GroupName.data).first()
		if current:
			raise ValidationError('This username has already been registered!')
	
class MyAccount(FlaskForm):
	FullName = StringField('Full Name')
	Username = StringField('Username', validators=[Length(min=5)])
	NewPass = PasswordField('New Password', validators=[Length(min=8, max=64)])
	ConfirmPass = PasswordField('Confirm Password', validators=[EqualTo('NewPass')])
	EMAIL = StringField('E-mail', validators=[Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
	Save = SubmitField('Save Changes')
	def validate_Email(self,Email):
		if Username.data != current_user.Username:
			current = User.query.filter_by(Email=Email.data).first()
			if current:
				raise ValidationError('This E-Mail has already been registered!')
	def validate_Username(self,Username):
		if Username.data != current_user.Username:
			current = User.query.filter_by(Username=Username.data).first()
			if current:
				raise ValidationError('Please enter a new username')

class EventsForm(FlaskForm):
	EventName = StringField('Event Name', validators=[Length(min=8, max=64)])
	Description = TextAreaField('Description', validators=[DataRequired()])
	Date = DateTimeField('Event Date', format="%d/%m/%y")
	Time = DateTimeField('Event Time', format="%H:%M")
	Invite = SubmitField('Create Event')
