from orbitus import db, login_manager
from flask_login import UserMixin
from sqlalchemy import func

@login_manager.user_loader
def load_user(user_id):
    return Main.query.get(user_id)


class GroupModel(db.Model):
	__tablename__ = 'GroupModel'
	id = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	Description = db.Column(db.String(120), nullable=False)
	default_picture = db.Column(db.String(20), default='default.jpg')
	users = db.relationship('User', backref='member',lazy=True)	

	def __repr__(self):
		return f"('{self.id}', '{self.groupname}', '{self.Description}', '{self.default_picture}','{self.main}')"
	

class User(db.Model, UserMixin):
	__tablename__	= 'User'
	id = db.Column(db.Integer, primary_key=True)
	FullName = db.Column(db.String(40), nullable=False)
	EMAIL = db.Column(db.String(120),unique=True, nullable=False)
	profile_pic = db.Column(db.String(20),nullable=False,default='default_pic.png')
	Username = db.Column(db.String(40),unique=True, nullable=False)
	Password = db.Column(db.String(64), nullable=False)
	#group = db.relationship('GroupModel', backref='member', lazy=True)
	group_id = db.Column(db.Integer,db.ForeignKey(GroupModel.id), nullable=True)
	def __repr__(self):
		return f"('{self.id}','{self.FullName}', '{self.EMAIL}', '{self.Username}','{self.profile_pic}','{self.Password}','{self.group_id}')"