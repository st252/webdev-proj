from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)

  from app.blueprints import main
  app.register_blueprint(main)
  db.init_app(app)
  login.init_app(app)

  return app

from app import routes, models
