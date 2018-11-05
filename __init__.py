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
crypter = Bcrypt(Orbitus) # Do not mess with this... Especially Kushagra
login_manager = LoginManager(Orbitus)

from orbitus import routes 