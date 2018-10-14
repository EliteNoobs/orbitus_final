from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Register, LogIn, Username, PersonalInfo

app = Flask(__name__)
app.config['SECRET_KEY'] = '137173d918599668dd83e68db2bcad2e'
#Added a basic Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String,unique=True, nullable=False)
	username = db.Column(db.String,unique=True, nullable=False)
	password = db.Column(db.String(64), nullable=False)

class Group(db.Model):
	groupid = db.Column(db.Integer, primary_key=True)
	groupname = db.Column(db.String(32), nullable=False)
	
	def __repr__(self):
		return f"('{self.name}', '{self.email}', '{self.username}')"
#It is not linked with the server yet.
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET','POST'])
def signin():
	SignInForm = LogIn()
	return render_template('signin.html', title='signin', form=SignInForm)

@app.route('/signup', methods=['GET','POST'])
def signup():
	SignUpForm = Register()
	if SignUpForm.validate_on_submit():
		return redirect(url_for('createuser'))
	return render_template('signup.html', title='signup', form=SignUpForm)

@app.route('/createuser', methods=['GET','POST'])
def createuser():
	User = Username()
	if User.validate_on_submit():
		return redirect(url_for('createuser2'))
	return render_template('createuser.html', title='createuser', form=User)

@app.route('/createuser2', methods=['GET','POST'])
def createuser2():
	Personal = PersonalInfo()
	if Personal.validate_on_submit():
		return redirect(url_for('dashboard'))
	return render_template('createuser2.html', title='createuser2', form=Personal)
	
@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
	return render_template('dashboard.html')

@app.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
