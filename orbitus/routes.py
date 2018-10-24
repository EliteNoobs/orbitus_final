from flask import render_template, flash, redirect, url_for
from orbitus.models import User, Group
from orbitus.forms import Register, LogIn, Username, PersonalInfo
from orbitus import Orbitus, db, crypter

@Orbitus.route('/')
@Orbitus.route('/index')
def index():
    return render_template('index.html')

@Orbitus.route('/signin', methods=['GET','POST'])
def signin():
	SignInForm = LogIn()
	return render_template('signin.html', title='signin', form=SignInForm)

@Orbitus.route('/signup', methods=['GET','POST'])
def signup():
	SignUpForm = Register()
	if SignUpForm.validate_on_submit():
		return redirect(url_for('createuser'))
	return render_template('signup.html', title='signup', form=SignUpForm)

@Orbitus.route('/createuser', methods=['GET','POST'])
def createuser():
	User = Username()
	if User.validate_on_submit():
		hashed_pw = crypter.generate_password_hash(User.Password.data).decode('utf-8')
		entry_user = Username(Username=User.Username.data, Password=User.Password.data)
		db.session.add(entry_user)
		db.session.commit()
		return redirect(url_for('createuser2'))
	return render_template('createuser.html', title='createuser', form=User)

@Orbitus.route('/createuser2', methods=['GET','POST'])
def createuser2():
	Personal = PersonalInfo()
	if Personal.validate_on_submit():
		return redirect(url_for('dashboard'))
	return render_template('createuser2.html', title='createuser2', form=Personal)
	
@Orbitus.route('/dashboard', methods=['GET','POST'])
def dashboard():
	return render_template('dashboard.html')

@Orbitus.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')  

