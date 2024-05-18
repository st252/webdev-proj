from app import app, db
from app.models import *
from flask_migrate import Migrate
from app.config import DeploymentConfig

app = create_app(DeploymentConfig)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Request': Request, 'Reply': Reply}
