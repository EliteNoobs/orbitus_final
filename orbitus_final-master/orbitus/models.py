from orbitus import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Main.get(user_id)


class Group(db.Model):
	groupid = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	
	
class Main(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	FullName = db.Column(db.String(40), nullable=False)
	EMAIL = db.Column(db.String(120),unique=True, nullable=False)
	Username = db.Column(db.String(40),unique=True, nullable=False)
	Age = db.Column(db.Integer, nullable=False)
	Password = db.Column(db.String(64), nullable=False)
	def __repr__(self):
		return f"('{self.FullName}', '{self.EMAIL}', '{self.Username}')"