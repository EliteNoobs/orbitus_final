from orbitus import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String, nullable=False)
	email = db.Column(db.String,unique=True, nullable=False)
	Username = db.Column(db.String,unique=True, nullable=False)
	password = db.Column(db.String(64), nullable=False)

class Group(db.Model):
	groupid = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	
	def __repr__(self):
		return f"('{self.fullname}', '{self.email}', '{self.Username}')"
	

#It is not linked with the server yet.