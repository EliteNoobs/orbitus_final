from orbitus import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String, nullable=False)
	email = db.Column(db.String,unique=True, nullable=False)
	Username = db.Column(db.String,unique=True, nullable=False)
	password = db.Column(db.String(64), nullable=False)
	
                def __repr__(self):
			return f"('{self.fullname}', '{self.email}', '{self.Username}')"


class Group(db.Model):
	groupid = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	
	
class Main(db.Model):
	FullName = StringField('Full Name', validators=[DataRequired()])
	EMAIL = StringField('E-Mail', validators=[DataRequired(), Email()])
	Username = StringField('Username', validators=[DataRequired(), Length(min=6)])
	Password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
	Age = IntegerField('Age', validators=[DataRequired(), Length(min=0)])

#Added Main Model
