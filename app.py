from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)
swagger = Swagger(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *
from routes import *
