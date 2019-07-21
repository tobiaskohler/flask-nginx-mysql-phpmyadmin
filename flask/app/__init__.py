from flask import Flask
from config import Config

####################################################
########Flask INSTANZ###############################

app = Flask(__name__)
app.config.from_object(Config)

####################################################
########SQLAlchemy INSTANZ##########################

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
Migrate(app, db)
