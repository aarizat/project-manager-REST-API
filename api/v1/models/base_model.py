from uuid import uuid4

from api.v1.extensions import db


class BaseModel:
    id = db.Column(db.String(60), primary_key=True)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        for k, v in kwargs.items():
            setattr(self, k, v)

    def as_dict(self):
        '''Return a dictionary with the attributes of a Project instance.
        '''
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }

    def save(self):
        '''Save an object in DB.
        '''
        db.session.add(self)
        db.session.commit()

    def delete(self):
        '''Delete an object from DB
        '''
        db.session.delete(self)
        db.session.commit()
