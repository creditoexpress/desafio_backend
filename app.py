from flask import Blueprint, Flask
from application.controllers.auth import auth
from application.controllers.loan import loan

application = Flask(__name__)
application.register_blueprint(auth, url_prefix='/api/auth')
application.register_blueprint(loan, url_prefix='/api/loan')

if __name__ == '__main__':
    application.run()
