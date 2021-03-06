from flask import render_template, flash, redirect, url_for, request
from orbitus.models import Group, Main
from orbitus.forms import Register, LogIn, Username, PersonalInfo, Group
from orbitus import Orbitus, db, crypter
from flask_login import login_required,login_user, current_user, logout_user, login_required


#Dummy user
d_user = Main()
db.create_all()

def FE(name,mail):
	d_user.FullName = name
	d_user.EMAIL = mail

def UP(uname,passwd):
	d_user.Username = uname
	d_user.Password = passwd

def A(age):
	d_user.Age = age

#These will put in the default values
def clear():
	d_user.FullName = ''
	d_user.EMAIL = ''
	d_user.Username = ''
	d_user.Password = ''
	d_user.Age = 10

clear()

@Orbitus.route('/')
@Orbitus.route('/index')
def index():
    return render_template('index.html')


@Orbitus.route('/signup', methods=['GET','POST'])
def signup():
	SignUpForm = Register() 	#These are the forms
	if SignUpForm.validate_on_submit():
		FE(name=SignUpForm.FullName.data,mail=SignUpForm.EMAIL.data)
 
		return redirect(url_for('createuser'))
	return render_template('signup.html', title='signup', form=SignUpForm)

@Orbitus.route('/createuser', methods=['GET','POST'])
def createuser():
	User = Username()	#These are the forms
	if User.validate_on_submit():
		hashed_pw = crypter.generate_password_hash(User.Password.data).decode('utf-8')
		UP(uname=User.Username.data, passwd=hashed_pw)
		db.session.add(d_user)
		db.session.commit()
		clear()
		return redirect(url_for('signin'))
	return render_template('createuser.html', title='createuser', form=User)

@Orbitus.route('/createuser2', methods=['GET','POST'])
def createuser2():
	Personal = PersonalInfo()	#These are the forms
	if Personal.validate_on_submit():
		#A(age=Personal.Age.data)
		#db.session.add(d_user)
		#db.session.commit()	
		clear()
		return redirect(url_for('dashboard'))
	return render_template('createuser2.html', title='createuser2', form=Personal)
	

@Orbitus.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    SignIn = LogIn()
    if SignIn.validate_on_submit():
    	user = Main.query.filter_by(Username=SignIn.Username.data).first()
    	if user and crypter.check_password_hash(user.Password, SignIn.Password.data):
        	login_user(user, remember=SignIn.RememberMe.data)
        	next_page = request.args.get('next')
       		return redirect(url_for('dashboard'))
		else:
	       flash('Login unsuccesfull. Please check your username and password.','Danger')
    return render_template('signin.html', title='Signin', form=SignIn)
 
@Orbitus.route('/creategroup', methods=['GET', 'POST'])
def creategroup():
	group = Group()
	return render_template('creategroup.html', title='Create Group', form=group)
	
@Orbitus.route('/searchgroup', methods=['GET', 'POST'])
def searchgroup():
	return render_template('searchgroup.html', title='Create Group')

@Orbitus.route('/signout')
def signout():
	logout_user()
	return redirect(url_for('signin'))

@Orbitus.route('/dashboard', methods=['GET','POST'])
def dashboard():
	return render_template('dashboard.html')

@Orbitus.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')
	
@Orbitus.route('/offline', methods=['GET','POST'])
def offline():
    return Orbitus.send_static_file('offline.html')
	
@Orbitus.route('/service-worker.js')
def sw():
    return Orbitus.send_static_file('service-worker.js')