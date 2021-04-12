from flask import Blueprint

api_views = Blueprint('api_views', __name__, url_prefix='/api/v1')


from api.v1.views.projects import *
from api.v1.views.tasks import *
from api.v1.views.projects_tasks import *
from api.v1.views.users import *

