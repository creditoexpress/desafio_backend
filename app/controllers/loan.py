from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from app.services.auth import Auth, JWT
from app.services.loan import Loan


loan = Blueprint('loan', __name__)


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


@loan.route('/simulation', methods=['POST'])
@token_required
def simulate(decode):

    request_data = request.get_json()
    response = Loan.simulate(request_data, decode)

    return jsonify(response)