from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#Changes Made - App name has become 'Orbitus' from 'app'
Orbitus = Flask(__name__)
Orbitus.config['SECRET_KEY'] = '137173d918599668dd83e68db2bcad2e'
#Added a basic Database
Orbitus.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Orbitus.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@127.0.0.1:8001/flask'
db = SQLAlchemy(Orbitus)
crypter = Bcrypt(Orbitus) # Encryption module
login_manager = LoginManager(Orbitus)

from orbitus import routes 

#Ashutosh don't shout at me, this is done to enable page not found function, its working. I have not broken the app.
def create_app(config_filename):
	Orbitus.register_error_handler(404, page_not_found)
	return Orbitus