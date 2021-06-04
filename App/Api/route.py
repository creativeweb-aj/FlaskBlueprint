from flask import Blueprint

# Blueprint for Api App
# This App route url start with '/api'
api = Blueprint('Api', __name__, url_prefix='/api')


# App routes are created below
@api.route('/user')
def user():
    return {'key': 'value'}
