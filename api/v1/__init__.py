'''
Factory function to init app.
'''
from flask import Flask

from api.v1.extensions import db
from api.v1.config import Config


def create_app(config_class=Config):
    '''
    Factory function.
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from api.v1.views import api_views
    app.register_blueprint(api_views)
    return app


from api.v1 import models

