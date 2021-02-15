"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask import Flask, request, make_response
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @swag_from("../swagger/user/GET.yml")
    def get(self):
        """ Return an user key information based on his name """
        user = UserRepository.get(public_id)
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(last_name, first_name, age):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(last_name, first_name, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(last_name=last_name, first_name=first_name, age=age)
        return jsonify({"user": user.json})

class RegisterResource(Resource):

    @swag_from("../swagger/register/POST.yml")
    def post(self):  
        data = request.get_json()  
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = UserRepository.create(email=data['email'], name=data['name'], password=hashed_password) 
        return new_user

class LoginResource(Resource):

    @swag_from("../swagger/login/POST.yml")
    def post(self):  
        auth = request.authorization  
        if not auth or not auth.username or not auth.password:  
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

        user = UserRepository.get(name=auth.username).first()   
            
        if not user:
            return {'message': f'User {username} doesn\'t exist'}, 500

        # user exists, comparing password and hash
        if UserRepository.verify_hash(data['password'], current_user.password):

            # generating access token and refresh token
            access_token = create_access_token(identity=username)

            refresh_token = create_refresh_token(identity=username)

            return {

                'message': f'Logged in as {username}',

                'access_token': access_token,

                'refresh_token': refresh_token

            }

        else:

            return {'message': "Wrong credentials"}, 500

class UserLogoutAccess(Resource):
    """
    User Logout Api 
    """

    @jwt_required
    def post(self):

        jti = get_raw_jwt()['jti']

        try:
            # Revoking access token
            revoked_token = RevokedTokenModel(jti=jti)

            revoked_token.add()

            return {'message': 'Access token has been revoked'}

        except:

            return {'message': 'Something went wrong'}, 500

class UserLogoutRefresh(Resource):
    """
    User Logout Refresh Api 
    """
    @jwt_refresh_token_required
    def post(self):

        jti = get_raw_jwt()['jti']

        try:

            revoked_token = RevokedTokenModel(jti=jti)

            revoked_token.add()

            pdb.set_trace()

            return {'message': 'Refresh token has been revoked'}

        except:

            return {'message': 'Something went wrong'}, 500

class TokenRefresh(Resource):
    """
    Token Refresh Api
    """

    @jwt_refresh_token_required
    def post(self):

        # Generating new access token
        current_user = get_jwt_identity()

        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}

