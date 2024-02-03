from flask_restx import Resource,Namespace
from api_models.user import user_post_model, user_model
from models.models import User
from config.conf import db,bcrypt

usr = Namespace("api")

@usr.route('/')
class Home(Resource):
    def get(self):
        return {'message':'hello from home route'}
    

@usr.route('/users')
class UsersApi(Resource):
    @usr.marshal_list_with(user_model)
    def get(self):
        return User.query.all()
        
    @usr.expect(user_post_model)
    @usr.marshal_with(user_model)
    def post(self):
        hashed_pw = bcrypt.generate_password_hash(usr.payload['password'])
        user = User(
            name=usr.payload['name'],
            email=usr.payload['email'],
            password=hashed_pw,

            )
        db.session.add(user)
        db.session.commit()

        return 'User created succesfully'
    
    
