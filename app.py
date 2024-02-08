from flask import Flask
from config.conf import api, db, bcrypt
from routes.users import usr
from routes.auth import auth
from models.models import *
from flask_jwt_extended import JWTManager
from os import environ


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/restxauthdb'
    app.config['JWT_SECRET_KEY']= environ.get('SECRET_KEY')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    api.init_app(app)
    jwt = JWTManager(app)

    api.add_namespace(usr)
    api.add_namespace(auth)
    

    return app

app = create_app()
