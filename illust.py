from flask_migrate import Migrate
from app import create_app, db
from app.config import DeploymentConfig
#from app.models import *

flaskApp = create_app(DeploymentConfig)
migrate = Migrate(flaskApp, db)

#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'User': User, 'Request': Request, 'Reply': Reply}
