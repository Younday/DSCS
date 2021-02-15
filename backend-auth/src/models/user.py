"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    public_id = db.Column(db.String(255))
    name = db.Column(db.String(50))
    password = db.Column(db.String(255))

    def __init__(self, public_id, email, name, password):
        """ Create a new User """
        self.public_id = public_id
        self.email = email
        self.name = name
        self.password = password
