from flask import Flask, render_template, flash, redirect, url_for
from forms import Register, LogIn, Username
app = Flask(__name__)

app.config['SECRET_KEY'] = '137173d918599668dd83e68db2bcad2e'

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
		flash(f'Congratulations! Account created for {User.Username.data}', 'success') #Under development (thesynthax - uncomment and pls check the issue. Its front end related my work here is done)
		return redirect(url_for('index'))
	return render_template('createuser.html', title='createuser', form=User)

@app.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
