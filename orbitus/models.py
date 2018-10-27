from orbitus import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(40))#, nullable=False)
	email = db.Column(db.String(40))#,unique=True, nullable=False)
	Username = db.Column(db.String(40))#,unique=True, nullable=False)
	password = db.Column(db.String(64))#, nullable=False)
	def __repr__(self):
		return f"('{self.fullname}', '{self.email}', '{self.Username}')"


class Group(db.Model):
	groupid = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	
	
class Main(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	FullName = db.Column(db.String(40))#, nullable=False)
	EMAIL = db.Column(db.String(40))#,unique=True, nullable=False)
	Username = db.Column(db.String(40))#,unique=True, nullable=False)
	Age = db.Column(db.Integer)#, nullable=False)
	Password = db.Column(db.String(64))#, nullable=False)