from flask_restx import Resource,Namespace
from config.conf import db,bcrypt
from models.models import User
from api_models.user import user_auth_model, user_model

auth = Namespace("api/auth")

@auth.route('/login')
class Login(Resource):
    @auth.expect(user_auth_model)
    def post(self):
        user = User.query.filter_by(email = auth.payload['email']).first()
        if user and bcrypt.check_password_hash(user.password, auth.payload['password']):
            return {'message':'Loged successfully'}
        
        else:
            return {'message':'invalid email or password'}