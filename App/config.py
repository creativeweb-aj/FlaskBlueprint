import os

# Configuration keys are set here
DEBUG = os.environ.get("DEBUG")
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
