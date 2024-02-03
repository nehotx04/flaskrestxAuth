from config.conf import db  

class User(db.Model):
    __tablename__  ='users'
    id = db.Column(db.Integer ,primary_key = True, autoincrement=True)
    email = db.Column(db.String(255),unique=True,nullable=False)
    name = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    tasks = db.relationship('Task', back_populates='user')

class Task(db.Model):
    __tablename__ ='tasks'
    id = db.Column(db.Integer , primary_key=True,autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean,nullable=False,default=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='tasks')
