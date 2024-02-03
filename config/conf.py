from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
api = Api()
db = SQLAlchemy()