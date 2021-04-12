'''
Decorator function to generate verify jwt token.
'''
from functools import wraps

from flask import request, jsonify
import jwt

from api.v1.models import User
from api.run import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        print('Printing toeken: ', token)
        if token is None:
            return jsonify({'message': 'Token is missing.'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(public_id=data['public_id']).first()
            if not user:
                jsonify({'message': 'Unauthorized Access'}), 401
        except:
            return jsonify({'message': 'Token is invalid.'}), 401
        return f(*args, **kwargs)
    return decorated

