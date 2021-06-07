import datetime
import json
from flask import Blueprint, Response, request, jsonify
from App.extension import db
from App.Api.schema import UserSchema
from App.Api.models import User
from App.Api.auth import RequiredAuthToken, GetJwtToken
from App.response import TokenType, StatusType, ResponseModal

# Blueprint for Api App
# This App route url start with '/api'
api = Blueprint('Api', __name__)


# App routes are created below
@api.route('/user', methods=["GET"])
@RequiredAuthToken
def user(current_user):
    print(current_user.id)
    users = User.query.all()
    schema = UserSchema()
    data = schema.dumps(users, many=True)
    result = ResponseModal(StatusType.success.value, data, 'Users data sent successfully')
    return Response(result, status=200)


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


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    # password = data['password']
    obj = User.query.filter_by(email=email).first()
    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    accessToken = GetJwtToken(obj, tokenTime)
    tokenTime = {"type": TokenType.refreshToken.value, "value": 1}
    refreshToken = GetJwtToken(obj, tokenTime)
    result = json.dumps({"access_token": accessToken, "refresh_token": refreshToken})
    return Response(result, status=200)


@api.route('/refresh-token', methods=['GET'])
@RequiredAuthToken
def refreshToken(current_user):
    userId = current_user.id
    obj = User.query.filter_by(id=userId).first()
    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    accessToken = GetJwtToken(obj, tokenTime)
    result = json.dumps({"access_token": accessToken})
    return Response(result, status=200)