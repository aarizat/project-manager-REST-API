'''
Model to represent a user in the project administrator.
'''
from werkzeug.security import generate_password_hash, check_password_hash

from api.v1.extensions import db


class User(db.Model):
    '''
    User model
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(80), unique=True, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

