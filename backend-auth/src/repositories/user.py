""" Defines the User repository """

from models import User
import uuid
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(name):
        """ Query a user by last and first name """
        return User.query.filter_by(name=name).one()

    @staticmethod
    def create(email, name, password):
        new_user = User(public_id=str(uuid.uuid4()), email=email, name=name, password=password)
        try:
            new_user.save()
            access_token = create_access_token(identity=name)
            refresh_token = create_refresh_token(identity=name)
            return {

                'message': f'User {name} was created',
                'access_token': access_token,

                'refresh_token': refresh_token

            }

        except Exception as e:

            return {'message': 'Something went wrong'}, 500

    @staticmethod
    def verify_hash(password, hash_):

        return sha256.verify(password, hash_)


