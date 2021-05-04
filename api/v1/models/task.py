'''
Model to represent tasks.
'''
from uuid import uuid4

from api.v1.models.base_model import BaseModel
from api.v1.extensions import db


class Task(BaseModel, db.Model):
    '''
    Task model
    '''
    __tablename__ = 'tasks'
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True, default='')
    execution_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(10), default='In process')
    project_id = db.Column(db.String(60), db.ForeignKey('projects.id'))

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)


