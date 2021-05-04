'''
Model to represent a project in the project manager.
'''
from api.v1.models.base_model import BaseModel
from api.v1.extensions import db


class Project(BaseModel, db.Model):
    '''
    Project model
    '''
    __tablename__ = 'projects'
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(10), default='In process')
    tasks = db.relationship('Task', cascade="all, delete", backref='project')

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)

