"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources.user import *

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/<string:last_name>/<string:first_name>",
)
Api(USER_BLUEPRINT).add_resource(
    LoginResource, "/login",
)
Api(USER_BLUEPRINT).add_resource(
    RegisterResource, "/register",
)
Api(USER_BLUEPRINT).add_resource(
    UserLogoutAccess, "/logout/access",
)
Api(USER_BLUEPRINT).add_resource(
    UserLogoutRefresh, "/logout/refresh",
)
Api(USER_BLUEPRINT).add_resource(
    TokenRefresh, "/token/refresh",
)
