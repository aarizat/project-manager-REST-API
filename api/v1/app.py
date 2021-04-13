'''
Run app.
'''
from flask import Flask

from api.v1.extensions import db
from api.v1.config import Config


app = Flask(__name__)
app.config.from_object(Config)

# init database
db.init_app(app)
with app.app_context():
    db.create_all()

# register blueprint
from api.v1.views import api_views
app.register_blueprint(api_views)

if __name__ == '__main__':
    app.run(debug=True)

#return app


#from api.v1 import models

