from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from api_models.task import task_post_model, task_model
from models.models import Task
from config.conf import db

task = Namespace('api/tasks')

@task.route('/')
class TaskList(Resource):
    @task.expect(task_post_model)
    @task.marshal_with(task_model)
    @jwt_required()
    def post(self):
        auth_id = get_jwt_identity()

        create_task = Task(
            title=task.payload['title'],
            description = task.payload['description'],
            user_id = auth_id
            )
        
        db.session.add(create_task)
        db.session.commit()
        return create_task
    
    @task.marshal_with(task_model)
    @jwt_required()
    def get(self):
        auth_id = get_jwt_identity()
        tasks = Task.query.filter_by(user_id=auth_id).all()
        return tasks
