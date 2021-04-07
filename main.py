from flask import Flask, jsonify, request
from src.controller.clients_controllers import clients_routes
from src.controller.loan_controllers import loan_routes
from src.service.clients_service import ClientsService
import src.exceptions as Exceptions

app = Flask(__name__)

app.register_blueprint(clients_routes, url_prefix='/clients')
app.register_blueprint(loan_routes, url_prefix='/loans')

@app.before_request
def check_auth_token():
    if request.path in ('/clients/auth', '/clients/'):
        return
    
    token = request.headers.get('Authorization')
    ClientsService().decode_auth_token(token)

@app.errorhandler(Exceptions.AlreadyExistsClientException)
def handleAlreadyExistsClientException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.InvalidClientBodyException)
def handleInvalidClientBodyException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.InvalidLoanBodyException)
def handleInvalidLoanBodyException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.ClientNotFoundException)
def handleClientNotFoundException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.InvalidCPFException)
def handleInvalidCPFException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.UnauthorizedException)
def handleUnauthorizedException(error):
    return get_json_error(error)

@app.errorhandler(Exceptions.UnableToAuthException)
def handleUnableToAuthException(error):
    return get_json_error(error)

def get_json_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')