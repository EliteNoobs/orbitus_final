import secrets
import os
from flask import render_template, flash, redirect, url_for, request
from orbitus.models import GroupModel, User, Events
from orbitus.forms import Register, LogIn, Username, GroupForm, MyAccount, EventsForm
from orbitus import Orbitus, db, crypter
from flask_login import login_required,login_user, current_user, logout_user, login_required

correctInfo = True #This is used to show the incorrect username or password error while signing in.

#Dummy user
d_user = User()
db.create_all()

def FE(name,mail):
	d_user.FullName = name
	d_user.EMAIL = mail

def UP(uname,passwd):
	d_user.Username = uname
	d_user.Password = passwd

#These will put in the default values
def clear():
	d_user.FullName = ''
	d_user.EMAIL = ''
	d_user.Username = ''
	d_user.Password = ''

clear()

@Orbitus.route('/')
@Orbitus.route('/index')
def index():
        global correctInfo
        correctInfo = True
        if current_user.is_authenticated:
        	return redirect(url_for('dashboard'))
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

@Orbitus.route('/creategroup', methods=['GET', 'POST'])
@login_required
def creategroup():
	Group = GroupForm()
	if Group.validate_on_submit():
		group_model = GroupModel()
		group_model.groupname = Group.GroupName.data
		group_model.Description = Group.Description.data
		db.session.add(group_model)
		db.session.commit()
		return redirect(url_for('dashboard'))
	return render_template('creategroup.html', title='Create Group', form=Group)


@Orbitus.route('/searchgroup', methods=['GET','POST'])
@login_required
def searchgroup():
	search = GroupModel()
	groups = search.query.all()
	#group_id = request.args.get('groupid',default=None,type=int)
	if request.method == "POST":
		button = request.form
		for key,value in button.items():
			current_group = GroupModel.query.filter_by(id=value).first()
			if len(current_group.users) < 30:
				current_user.group_id = value
				db.session.commit()
			else:
				return(redirect(url_for('dashboard')))
	return render_template('searchgroup.html', title='searchgroup', groups=groups)#, current=current_user)


@Orbitus.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(Username=form.Username.data).first()
        global correctInfo
        if user and crypter.check_password_hash(user.Password, form.Password.data):
            correctInfo = True
            login_user(user, remember=form.RememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            correctInfo = False
            flash('Signin Unsuccessful. Please check Username and password', 'danger')
    return render_template('signin.html', title='Signin', form=form, value=correctInfo) #This variable will be used in HTML to see if user has entered correct details or not


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(Orbitus.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)
	return picture_fn
 
@Orbitus.route('/myaccount', methods=['GET', 'POST'])
@login_required
def myaccount():
	account = MyAccount()
	if  form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.profile_pic = picture_file
		current_user.Username = form.Username.data
		current_user.EMAIL = form.EMAIL.data
		current_user.FullName = form.FullName.data
		db.session.commit()
		flash('Your Account has been updates!')
		return redirect(url_for('myaccount'))
	elif request.method == 'GET':
		form.Username.data = current_user.Username
		form.EMAIL.data = current_user.EMAIL
		form.FullName.data = current_user.FullName
	profile_pic = url_for('static', filename='profile_pics/' + current_user.profile_pic)
	return render_template('myaccount.html', title='Account', form=account, profile_pic=profile_pic)

@Orbitus.route('/hostanevent', methods = ['GET', 'POST'])
@login_required
def hostanevent():
	form = EventsForm()
	if form.validate_on_submit():
		event = Events(EventName=form.EventName.data, Description=form.Description.data)
		db.session.add(event)
		db.session.commit()
		flash('Your Event has been created!', 'success')	
		return redirect(url_for('dashboard'))
	return render_template('hostanevent.html', title='Event', form=form)


@Orbitus.route('/signout')
def signout():
	logout_user()
	return redirect(url_for('signin'))

@Orbitus.route('/dashboard', methods=['GET','POST'])
@login_required
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

#This is the page not found page
@Orbitus.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404