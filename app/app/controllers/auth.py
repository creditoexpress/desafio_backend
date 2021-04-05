from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from app.services.auth import Auth, JWT
from app.services.cpf import validate_cpf


auth = Blueprint('auth', __name__)


def token_required(function):
    
    @wraps(function)
    def decorated(*args, **kwargs):

        if 'Authorization' in request.headers and request.headers['Authorization']:
            user_data = JWT.decode(request.headers['Authorization'])

            if not user_data:
                return make_response({'status': 401, 'message': 'Invalid token'}, 401)
        
        else:
            return make_response({'status': 401,'message' : 'Missing token'}, 401)

        return function(user_data, *args, **kwargs)

    return decorated


@auth.route('/identify', methods=['POST'])
def login():
    
    request_data = request.get_json()

    if 'cpf' in request_data and 'celular' in request_data:
        if not validate_cpf(request_data['cpf']):
            response = {'status': 200, 'message':'CPF inválido'}
            return jsonify(response)
        if len(request_data['celular']) not in [10, 11]:
            response = {'status': 200, 'message':'Celular inválido'}
            return jsonify(response)
    else:
        response = {'status': 200, 'message':'CPF e/ou celular em branco'}

    response = Auth.identify(request_data)

    return jsonify(response)


@auth.route('/getCurrentUser')
@token_required
def current_user(decoded):
    
    return jsonify(decoded)