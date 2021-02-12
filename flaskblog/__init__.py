from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blog:enateye05@aadkyxw3e0k8ep$e0k8ep.coxgdsu0jfsg.us-west-2.rds.amazonaws.com/https://us-west-2.console.aws.am$aws.amazon.com/rds/home?region=us-west-2#database:id=aadkyxw3e0k8ep;is-cluster=f$'
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
