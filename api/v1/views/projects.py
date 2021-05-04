'''
Definition of endpoints to manage resources related to projects.
'''
from datetime import datetime, date

from flask import request, jsonify, Response

from api.v1.extensions import db
from api.v1.jwt import token_required
from api.v1.models import Project
from api.v1.views import api_views


DATE_FMT = '%Y-%m-%d'


@api_views.route('/projects', strict_slashes=False, methods=['GET'])
@token_required
def get_projects():
    '''
    List all of project resources
    '''
    projects = Project.query.all()
    return jsonify([project.as_dict() for project in projects])


@api_views.route('/projects/<id>', strict_slashes=False, methods=['GET'])
@token_required
def get_project_by_id(id):
    '''
    Fecth a project resource by its id.
    '''
    project = Project.query.get_or_404(id)
    return jsonify(project.as_dict())


@api_views.route('/projects', strict_slashes=False, methods=['POST'])
@token_required
def create_project():
    '''
    Create a project resource
    '''
    json = request.get_json()
    start_date = datetime.strptime(json.get('start_date'), DATE_FMT).date()
    if start_date < date.today():
        return {"start_date": 'should match or exceed the current date'}, 422
    if json.get('end_date'):
        end_date = datetime.strptime(json.get('end_date'), DATE_FMT).date()
        if end_date <= date.today():
            return {"end_date": 'must be greater than the current date'}, 422
    project = Project(**json)
    project.save()
    return jsonify(project.as_dict()), 201


@api_views.route('/projects/<id>', strict_slashes=False, methods=['DELETE'])
@token_required
def delete_project_by_id(id):
    '''
    Delete a project resource by ID.
    '''
    project = Project.query.get_or_404(id)
    project.delete()
    return jsonify({"Deleted": id})


@api_views.route('/projects/<id>', strict_slashes=False, methods=['PUT'])
@token_required
def update_project_by_id(id):
    '''
    Update a project resource by ID.
    '''
    project = Project.query.get_or_404(id)
    json = request.get_json()
    for key, value in json.items():
        if key not in ('start_date', 'end_date', 'status'):
            setattr(project, key, value)
    db.session.commit()
    if json.get('end_date'):
        end_date = datetime.strptime(json['end_date'], DATE_FMT).date()
        if end_date < project.start_date:
            return {'end_date': 'cannot be less than start_date project'}, 422
        for task in project.tasks:
            if task.execution_date > end_date:
                response = {
                    'task_id': task.id,
                    'execution_date': task.execution_date,
                    'msg': 'task with a prior date to end date project'
                }
                return jsonify(response), 422
        project.end_date = json['end_date']
        db.session.commit()
    if json.get('status') == 'Finished':
        for task in project.tasks:
            if task.status != 'Finished':
                response = {
                    'task_id': task.id,
                    'status': task.status,
                    'msg': 'This task must be completed'
                }
                return jsonify(response), 422
        project.status = json['status']
        db.session.commit()
    return jsonify(project.as_dict())


@api_views.route('/projects/<id>', strict_slashes=False, methods=['PATCH'])
@token_required
def modify_project_by_id(id):
    '''
    Update a project resource by ID.
    '''
    project = Project.query.get_or_404(id)
    json = request.get_json()
    for key, value in json.items():
        if key not in ('start_date', 'end_date', 'status'):
            setattr(project, key, value)
    db.session.commit()
    if json.get('end_date'):
        end_date = datetime.strptime(json.get('end_date'), DATE_FMT).date()
        if end_date < project.start_date:
            return {'end_date': 'cannot be less than start_date project'}, 422
        for task in project.tasks:
            if task.execution_date > end_date:
                response = {
                    'task_id': task.id,
                    'execution_date': task.execution_date,
                    'msg': 'task with a prior date to end date project'
                }
                return jsonify(response), 422
        project.end_date = json.get('end_date')
        db.session.commit()
    if json.get('status') == 'Finished':
        for task in project.tasks:
            if task.status != 'Finished':
                response = {
                    'task_id': task.id,
                    'status': task.status,
                    'msg': 'This task must be completed'
                }
                return jsonify(response), 422
        project.status = json['status']
        db.session.commit()
    return jsonify(project.as_dict())
