import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from base.core.config import settings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

# app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop123456'
app.config['SECRET_KEY'] = settings.JWT_SECRET_KEY
app.config['SQLALCHEMY_ECHO'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI + settings.DATABASE_NAME
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.debug = True

from base import features
