from flask import Flask

from App.Api.route import api
from App.Admin.route import admin


# All Apps routes are registered here
def create_app():
    app = Flask(__name__)
    # Api App
    app.register_blueprint(api)
    # Admin App
    app.register_blueprint(admin)
    # Return App for run in run.py file
    return app
