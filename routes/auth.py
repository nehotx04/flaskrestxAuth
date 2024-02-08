from flask_restx import Resource,Namespace
from config.conf import db,bcrypt
from models.models import User
from api_models.user import user_auth_model, user_model
from flask_jwt_extended import create_access_token

auth = Namespace("api/auth")

@auth.route('/login')
class Login(Resource):
    @auth.expect(user_auth_model)
    def post(self):
        user = User.query.filter_by(email = auth.payload['email']).first()
        if user and bcrypt.check_password_hash(user.password, auth.payload['password']):
            token = create_access_token(identity=user.id)
            
            return {'message':'Loged successfully', "token": token}
        
        else:
            return {'message':'invalid email or password'}, 401 