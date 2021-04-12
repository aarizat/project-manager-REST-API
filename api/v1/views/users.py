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
from api.v1.extensions import db
from api.run import app


@api_views.route('/users/signup', strict_slashes=False, methods=['POST'])
def signup():
    '''
    Register a new user in the project administrator.
    '''
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        user = User(
            email=data['email'],
            public_id=str(uuid4()),
            username=data['username'],
            password=generate_password_hash(data['password'])
        )
        db.session.add(user)
        db.session.commit()
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
    user = User.query\
        .filter_by(username=auth.get('username'))\
        .first()
    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist."'}
        )
    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=1)
        }, app.config['SECRET_KEY'])
        return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password."'}
    )

