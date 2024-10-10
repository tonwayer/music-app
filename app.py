from flask import Flask
from flask_migrate import Migrate
from config import Config
from flasgger import Swagger
from models import db
from routes import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

swagger = Swagger(app)

migrate = Migrate(app, db)

from models import *

register_blueprints(app)
