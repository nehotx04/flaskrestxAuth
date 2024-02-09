from flask_restx import Namespace, Resource,marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from api_models.task import task_post_model, task_model
from models.models import Task
from config.conf import db

task = Namespace('api/tasks')

def vAuth(id):
    if get_jwt_identity() != id:
        return False
    else:
        return True

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

@task.route('/<int:id>')
class TaskId(Resource):
    @jwt_required()
    def get(self,id):
        tsk = Task.query.filter_by(id = id).first()
        if tsk:
            if vAuth(tsk.user_id):
                return marshal(tsk,task_model),200
        
            else:
                return {"message":"unauthorized"},401
        else:
            return {"message":"Task id not found"}
    
    @task.expect(task_post_model)
    @jwt_required()
    def put(self,id):
        tsk = Task.query.filter_by(id = id).first()
        if tsk:
            if vAuth(tsk.user_id):
                tsk.title = task.payload['title']
                tsk.description = task.payload['description']
                db.session.commit()
                return marshal(tsk,task_model),202
            else:
                return {"message":"unauthorized"},401
        else:
            return {"message":"Task id not found"}

    @jwt_required()
    def delete(self,id):
        tsk = Task.query.filter_by(id = id).first()
        if tsk:
            if vAuth(tsk.user_id):
                db.session.delete(tsk)
                db.session.commit()
                return {"message":"Task deleted successfully"},204
            else:
                return {"message":"unauthorized"},401
        else:
            return {"message":"Task id not found"}
