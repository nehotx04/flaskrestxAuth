from flask_restx import fields 
from config.conf import api

task_post_model = api.model("User",{
    'title':fields.String,
    'description':fields.String,
    'user_id':fields.Integer
    }
)

task_model = api.model("User",{
    'id':fields.Integer,
    'title':fields.String,
    'description':fields.String,
    'completed':fields.Boolean,
    'user_id':fields.Integer
    }
)