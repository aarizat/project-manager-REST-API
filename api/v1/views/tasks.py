'''
Endpoint to manahe all of task in the project manager.
'''
from api.v1.extensions import db
from api.v1.jwt import token_required
from api.v1.models import Task
from api.v1.views import api_views

from flask import jsonify, request


@api_views.route('/tasks', strict_slashes=False, methods=['GET'])
@token_required
def get_tasks():
    '''
    List of task in the project manager.
    '''
    tasks = Task.query.all()
    return jsonify([task.as_dict() for task in tasks])

