import os

# Configuration keys are set here
SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

CELERY_BACKEND = os.environ.get('CELERY_BACKEND')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

