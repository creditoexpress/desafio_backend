from flask import Blueprint, request

import json

from controller import user as user_controller
from auth import user as user_auth

user_routes = Blueprint( 'user', __name__, url_prefix = '/user' )

@user_routes.route( '/insert', methods = ['POST'] )
def insert_users():
    return user_controller.insert_users( request.get_json() )

@user_routes.route( '/insert-file', methods = ['POST'] )
def insert_users_by_file():
    file = json.load( request.files[ 'file' ] )
    return user_controller.insert_users( file )

@user_routes.route( '/login', methods = ['GET'] )
@user_auth.generate_user_token
def login():
    return user_controller.get_user_id_by_cpf_and_cellphone( request.get_json() )
