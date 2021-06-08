from flask import jsonify, request, Response
from App.Api.models import User
from functools import wraps
import jwt
import os
import json
import datetime
from App.response import TokenType

SECRET_KEY = os.environ.get('SECRET_KEY')


# decorator for verifying the JWT access token
def RequiredAuthToken(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.split(' ')[1]
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, 'utf-8')
            current_user = User.query \
                .filter_by(id=data['user_id'], is_active=True, is_verify=True, is_delete=False) \
                .first()
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message': 'Token is expired !!'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated


def GetJwtToken(data, tokenTime):
    value = tokenTime.get('value')
    if tokenTime.get('type') == TokenType.accessToken.value:
        payload = {'user_id': data.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=value)}
    else:
        payload = {'user_id': data.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=value)}
    token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
    # result = json.dumps({"access_token": str(token)})
    return token




