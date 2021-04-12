'''
Model to represent a project in the project manager.
'''
from api.v1.extensions import db


class Project(db.Model):
    '''
    Project model
    '''
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(10), default='In process')
    tasks = db.relationship('Task', cascade="all, delete", backref='project')

    def as_dict(self):
        '''
        Return a dictionary with the attributes of a Project instance.
        '''
        to_dict = {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
        return to_dict

