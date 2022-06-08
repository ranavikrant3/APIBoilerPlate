from flask import Flask, redirect, url_for
from flask_script import Manager, Server
from src.server.config.config import DevelopmentConfig, Network
from src.server.managers import database, admin, views, logger
from src.server.managers.database import db
from src.server.models.pmk_guidebookskills import GuidebookSkills

app = Flask(__name__, static_url_path='/', static_folder='static', template_folder='templates')

app.config.from_mapping(DevelopmentConfig)
app.config.from_pyfile('config/config.py')

# Flask script command
manager = Manager(app)
# Flask development web server
manager.add_command("runserver", Server(host=Network.get('inet-address'), port=Network.get('port')))

# Initialise the database
database.init_app(app)

# Initialize the Flask-Admin package
admin.init_app(app)

# Initialise the Logger
logger.init_app(app)

# Initialize the view
views.init_app(app)

'''

with app.app_context():
    db.drop_all()
    db.create_all()

'''

@app.route('/')
def index():
    return redirect(url_for('admin.index'))