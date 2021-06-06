from flask import Flask
from App.Api.router import api
from App.Admin.router import admin
from App.extension import db, migrate
from App.config import DEBUG, HOST, PORT


# All Apps routes are registered here
def create_app(config_file="config.py"):
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')

    # All configuration are in config file
    app.config.from_pyfile(config_file)

    # Database connection initialize
    db.init_app(app)

    # Database migrate initialize
    migrate.init_app(app, db)

    # Return App for run in run.py file
    return app


if __name__ == "__main__":
    create_app().run(debug=DEBUG, host=HOST, port=PORT)
