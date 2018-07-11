from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import os

#from flask_scss import Scss
#Scss(app, static_dir='app/static/assets/css', asset_dir='app/static/assets/scss')

# Initialize the app
#app = Flask(__name__, instance_relative_config=True)
application = Flask(__name__)


# Load the config file
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)


login = LoginManager(application)
login.login_view = 'login'
# 'login' is the view function that handles log ins

application.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='mdstest10010011@gmail.com',
    MAIL_PASSWORD=os.environ['MAIL_PASSWORD'],

)

mail = Mail(application)

from application import views, models



