from orbitus import db, login_manager
from flask_login import UserMixin
from sqlalchemy import func

@login_manager.user_loader
def load_user(user_id):
    return Main.get(user_id)


class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	description = db.Column(db.String(120), nullable=False)
	default_picture = db.Column(db.String(20), default='default.jpg')
	member_id = db.Column(db.Integer, db.ForeignKey('main.id'), nullable=False)

	def __repr__(self):
		return f"('{self.id}', '{self.groupname}', '{self.description}'')"


class Main(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	FullName = db.Column(db.String(40), nullable=False)
	EMAIL = db.Column(db.String(120),unique=True, nullable=False)
	Username = db.Column(db.String(40),unique=True, nullable=False)
	Age = db.Column(db.Integer, nullable=False)
	Password = db.Column(db.String(64), nullable=False)
	group = db.relationship('Group', backref='member', lazy=True)
	def __repr__(self):
		return f"('{self.FullName}', '{self.EMAIL}', '{self.Username}')"

