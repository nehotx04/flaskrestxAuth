from flask import Flask
from config.conf import api, db, bcrypt
from routes.users import usr
from models.models import *



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/restxauthdb'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    api.init_app(app)
    api.add_namespace(usr)



    return app

app = create_app()