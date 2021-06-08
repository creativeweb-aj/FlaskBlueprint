from flask import Flask
from App.extension import db, migrate, ma, swagger
from App.config import DEBUG, HOST, PORT
from App.Api.router import api
from App.Admin.router import admin


# All Apps routes are registered here
def create_app(config_file="config.py"):
    # Flask app initialize
    app = Flask(__name__)

    # All configuration are in config file
    app.config.from_pyfile(config_file)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')

    # Database connection initialize
    db.init_app(app)

    # Database migrate initialize
    migrate.init_app(app, db)

    # Marshmallow initialize
    ma.init_app(app)

    # Swagger initialize

    swagger.init_app(app)

    # Return App for run in run.py file
    return app


if __name__ == "__main__":
    create_app().run(debug=DEBUG, host=HOST, port=PORT)
