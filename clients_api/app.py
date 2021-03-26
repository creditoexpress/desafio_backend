from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from decouple import config

from api.routes import create_routes

from tools.load_data import seeders

import os

### Path criado para ser acessado em outros files
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

### Default MongoDB Configuration
default_config = {
    'MONGODB_SETTINGS': {
        'db': 'desafio_bd',
        'host': 'desafio_mongodb',
        'port': 27017,
        'username': config("MONGODB_USERNAME"),
        'password': config("MONGODB_PASSWORD"),
        'authentication_source': 'admin'
    },
    'ENV': 'development',
    'DEBUG': 'True'
}

def get_flask_app(config: dict = None) -> app.Flask:
    """
    Inicializa o app com as configurações desejada.
    Entrada padrão aponta para wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # Inicia Flask
    flask_app = Flask(__name__)

    # Configura app
    config = default_config if config is None else config
    flask_app.config.update(config)

    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    # init mongoengine
    ### db.app.config['MONGODB_SETTINGS']['db']
    db = MongoEngine(app=flask_app)

    # Alimenta banco 
    seeders(ROOT_DIR)

    return flask_app

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()

    app.run(host='0.0.0.0', port=5002)