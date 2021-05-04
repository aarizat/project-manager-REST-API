'''
Definition of endpoint to manage login and signup of users.
'''
from datetime import datetime, timedelta
from uuid import uuid4

from flask import make_response, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from api.v1.views import api_views
from api.v1.models import User
from api.v1.app import app


@api_views.route('/users/signup', strict_slashes=False, methods=['POST'])
def signup():
    '''
    Register a new user in the project administrator.
    '''
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        user = User(**data)
        user.save()
        return make_response('Successfully registered.', 201)
    return make_response('User already exists. Please Log in.', 202)


@api_views.route('/users/login', strict_slashes=False, methods=['POST'])
def login():
    '''
    Login users in the project administrator.
    '''
    auth = request.get_json()
    if not auth.get('username') or not auth.get('password'):
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required."'}
        )
    user = User.query.filter_by(username=auth.get('username')).first()
    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist."'}
        )
    if check_password_hash(user.password, auth.get('password')):
        exp = datetime.utcnow() + timedelta(minutes=30)
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': exp
        }, app.config['SECRET_KEY'])
        return make_response(
            jsonify({
                'token': token.decode('UTF-8'),
                'Expire': exp.strftime('%d-%m-%Y %H:%M')
            }), 201)
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password."'}
    )
