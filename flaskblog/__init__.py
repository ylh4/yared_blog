from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    db.init_app(application)
    bcrypt.init_app(application)
    login_manager.init_app(application)
    mail.init_app(application)
    migrate.init_app(application, db)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    application.register_blueprint(users)
    application.register_blueprint(posts)
    application.register_blueprint(main)
    application.register_blueprint(errors)

    return application
