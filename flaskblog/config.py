import os
from dotenv import load_dotenv
# Absolute directory path
basedir = os.path.abspath(os.path.dirname(__file__))
# Looks for and loads .env file
# Can access env variables using os.environ.get(<VARNAME>)
load_dotenv(os.path.join(basedir, '.env'))

class Config:
     # ~~ Migration Repository ~~ #
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
