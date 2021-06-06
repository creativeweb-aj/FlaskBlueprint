import json

from flask import Blueprint, Response, request
from App.extension import db
from App.Api.schema import UserSchema
from App.Api.models import User

# Blueprint for Api App
# This App route url start with '/api'
api = Blueprint('Api', __name__)


# App routes are created below
@api.route('/user', methods=["GET"])
def user():
    users = User.query.all()
    print(users)
    schema = UserSchema()
    data = schema.dumps(users, many=True)
    print(data)
    return Response(data, status=200)


@api.route('/createuser', methods=["POST"])
def createuser():
    # Get data and jsonify it
    data = request.get_json()
    # Get key data from data
    username = data['username']
    email = data['email']
    password = data['password']
    obj = User(username=username, email=email, password=password)
    db.session.add(obj)
    db.session.commit()
    userObj = User.query.get(obj.id)
    schema = UserSchema()
    user = schema.dumps(userObj)
    return Response(user, status=200)
