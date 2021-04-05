from flask import Blueprint, Flask
from flask_cors import CORS
from os import environ

from application.controllers.auth import auth
from application.controllers.loan import loan


application = Flask(__name__)
CORS(application)
application.register_blueprint(auth, url_prefix='/api/auth')
application.register_blueprint(loan, url_prefix='/api/loan')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 80)))