from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger


# DB initialize in __init__ file
# db variable use for create models from here
db = SQLAlchemy()

# Migrate initialize in __init__ file
# Migrate database config
migrate = Migrate()

# Marshmallow for database model schema
ma = Marshmallow()

# Swagger initialize document
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    #"static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/doc"
}
SWAGGER_TEMPLATE = {
   "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}}
}
swagger = Swagger(config=swagger_config, template=SWAGGER_TEMPLATE)

