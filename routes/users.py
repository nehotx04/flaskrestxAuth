from flask_restx import Resource,Namespace
from api_models.user import user_post_model, user_model
from models.models import User
from config.conf import db,bcrypt

usr = Namespace("api/users")

@usr.route('/')
class UsersListApi(Resource):
    @usr.marshal_list_with(user_model)
    def get(self):
        return User.query.all()
        
    @usr.expect(user_post_model)
    @usr.marshal_with(user_model)
    def post(self):
        hashed_pw = bcrypt.generate_password_hash(usr.payload['password']).decode('utf-8')
        user = User(
            name=usr.payload['name'],
            email=usr.payload['email'],
            password=hashed_pw,

            )
        db.session.add(user)
        db.session.commit()

        return user
    
@usr.route('/<int:id>')
class UsersApi(Resource):
    @usr.marshal_list_with(user_model)
    def get(self, id):
        user = User.query.get(id)
        return user
    
    @usr.expect(user_post_model)
    @usr.marshal_with(user_model)
    def put(self,id):
        user = User.query.get(id)
        user.name = usr.payload['name']
        user.email = usr.payload['email']
        if usr.payload['password'] == '':

            user.password = user.password

        else:
            hashed_pw = bcrypt.generate_password_hash(usr.payload['password']).decode('utf-8')
            user.password = hashed_pw

        db.session.commit()

        return user
    
    def delete(self,id):
        user=User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"user deleted successfully"}
    
