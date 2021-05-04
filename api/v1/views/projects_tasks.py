'''
Define all of endpoint to manage tasks related to each project.
'''
from datetime import datetime

from flask import request, jsonify

from api.v1.extensions import db
from api.v1.jwt import token_required
from api.v1.models import Project, Task
from api.v1.views import api_views


DATE_FMT = '%Y-%m-%d'


@api_views.route('/projects/<project_id>/tasks',
                 strict_slashes=False, methods=['POST'])
@token_required
def add_task2project(project_id):
    '''
    Add a new task resource to a Project.
    '''
    json = request.get_json()
    project = Project.query.filter_by(id=project_id).first_or_404()
    if json.get('execution_date'):
        exec_date = datetime.strptime(json.get('execution_date'), DATE_FMT)
        if exec_date < project.start_date or exec_date > project.end_date:
            response = {
                'execution_date': json.get('execution_date'),
                'Msg': 'task date out of the project start and end date'
            }
            return jsonify(response), 422
    task = Task(**json)
    if task not in project.tasks:
        project.tasks.append(task)
        db.session.commit()
    return jsonify(task.as_dict()), 201


@api_views.route('/projects/<project_id>/tasks',
                 strict_slashes=False, methods=['GET'])
@token_required
def get_tasks_from_project(project_id):
    '''
    Fetch all of task resources from a Project
    '''
    project = Project.query.filter_by(id=project_id).first_or_404()
    project_dict = project.as_dict()
    project_dict['tasks'] = [task.as_dict() for task in project.tasks]
    return jsonify(project_dict), 200


@api_views.route('/projects/<project_id>/tasks/<task_id>',
                 strict_slashes=False, methods=['GET'])
@token_required
def fecth_task_from_project(project_id, task_id):
    '''
    Delete a task resource from a Project
    '''
    project = Project.query.filter_by(id=project_id).first_or_404()
    task = Task.query.filter_by(id=task_id).first_or_404()
    return jsonify(task.as_dict()), 200


@api_views.route('/projects/<project_id>/tasks/<task_id>',
                 strict_slashes=False, methods=['DELETE'])
@token_required
def delete_task_from_project(project_id, task_id):
    '''
    Delete a task resource from a Project
    '''
    project = Project.query.filter_by(id=project_id).first_or_404()
    task = Task.query.filter_by(id=task_id).first_or_404()
    if task in project.tasks:
        project.tasks.remove(task)
        db.session.commit()
    return jsonify({"Task deleted": task_id}), 200


@api_views.route('/projects/<project_id>/tasks/<task_id>',
                 strict_slashes=False, methods=['PATCH'])
@token_required
def update_task_from_project(project_id, task_id):
    '''
    Change the status of task resource from `In process` to `Finished`
    '''
    project = Project.query.filter_by(id=project_id).first_or_404()
    task = Task.query.filter_by(id=task_id).first_or_404()
    json = request.get_json()
    for k, v in json.items():
        if k != 'status' and k != 'execution_date':
            setattr(task, k, v)
        if k == 'status' and v == 'Finished':
            task.status = "Finished"
    db.session.commit()
    if json.get('execution_date'):
        exec_date = datetime.strptime(json.get('execution_date'), DATE_FMT)
        if exec_date < project.start_date or exec_date > project.end_date:
            response = {
                'execution_date': json.get('execution_date'),
                'Msg': 'task date out of the project start and end date'
            }
            return jsonify(response), 422
        task.execution_date = json.get('execution_date')
        db.session.commit()
    return jsonify(task.as_dict())


@api_views.route('/projects/<project_id>/tasks/<task_id>',
                 strict_slashes=False, methods=['PUT'])
@token_required
def modify_task_from_project(project_id, task_id):
    '''
    Change the status of task resource from `In process` to `Finished`
    '''
    project = Project.query.filter_by(id=project_id).first_or_404()
    task = Task.query.filter_by(id=task_id).first_or_404()
    json = request.get_json()
    for k, v in json.items():
        if k != 'status' and k != 'execution_date':
            setattr(task, k, v)
        if k == 'status' and v == 'Finished':
            task.status = "Finished"
    db.session.commit()
    if json.get('execution_date'):
        exec_date = datetime.strptime(json.get('execution_date'), DATE_FMT)
        if exec_date < project.start_date or exec_date > project.end_date:
            response = {
                'execution_date': json.get('execution_date'),
                'Msg': 'task date out of the project start and end date'
            }
            return jsonify(response), 422
        task.execution_date = json.get('execution_date')
        db.session.commit()
    return jsonify(task.as_dict())
