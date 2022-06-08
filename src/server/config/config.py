import os
import json


# Define the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# This is kept for debug mode for SQLAlchemy
# SQLALCHEMY_ECHO = True

with open(basedir + "/standalone.json") as json_file:
    standalone = json.load(json_file)

# Logger configurations
Logger = standalone.get('pmk-logger')

# Network configurations
Network = standalone.get('interfaces')

# Development configurations
DevelopmentConfig = standalone.get('profile').get('DevelopmentConfig')
