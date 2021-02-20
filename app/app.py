import os
from flask import Flask, request, jsonify, Response
from flask_restful import Api
from flask_jwt_extended import JWTManager

from recursos.rotas import initialize_routes
from db.db import initialize_db

application = Flask(__name__)
application.config.from_envvar('ENV_FILE_LOCATION')

api = Api(application)
jwt = JWTManager(application)

application.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
}

initialize_db(application)
initialize_routes(api)

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)