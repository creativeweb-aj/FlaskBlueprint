from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# DB initialize in __init__ file
# db variable use for create models from here
db = SQLAlchemy()

# Migrate initialize in __init__ file
# Migrate database config
migrate = Migrate()
