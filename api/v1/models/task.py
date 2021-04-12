'''
Model to represent tasks.
'''
from api.v1.extensions import db


class Task(db.Model):
    '''
    Task model
    '''
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True, default='')
    execution_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(10), default='In process')
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def as_dict(self):
        '''
        Return a dict with the attributes of a Task instance.
        '''
        to_dict = {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
        return to_dict

