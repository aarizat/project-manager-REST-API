'''
Model to represent a user in the project administrator.
'''
from uuid import uuid4
from werkzeug.security import generate_password_hash

from api.v1.models.base_model import BaseModel
from api.v1.extensions import db


class User(BaseModel, db.Model):
    '''
    User model
    '''
    __tablename__ = 'users'
    public_id = db.Column(db.String(80), unique=True, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        self.public_id = str(uuid4())
        self.password = generate_password_hash(kwargs.get('password'))
        kwargs.pop('password')
        BaseModel.__init__(self, *args, **kwargs)
