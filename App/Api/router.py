from flask import Blueprint, Response, json
from App.Api.models import *

# Blueprint for Api App
# This App route url start with '/api'
api = Blueprint('Api', __name__)


# App routes are created below
@api.route('/user', methods=["GET"])
def user():
    data = {"key": "value", "name": "ajay"}
    data = json.dumps(data)
    return Response(data, status=200)
