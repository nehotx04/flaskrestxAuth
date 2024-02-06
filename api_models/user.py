from flask_restx import fields 
from config.conf import api

user_post_model = api.model("User",{
    'email':fields.String,
    'name':fields.String,
    'password':fields.String
    }
)

user_model = api.model("User",{
    'id':fields.Integer,
    'email':fields.String,
    'name':fields.String,
    'password':fields.String
    }
)

user_auth_model = api.model("User",{
    'email': fields.String,
    'password': fields.String,
})