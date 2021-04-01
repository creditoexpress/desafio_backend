# import os
from src.ext.nosql import nosql
from src import routes
from src.conf import conf
from flask import Flask

def create_app():
    application = Flask(__name__)


    db = nosql.init_app(application)
    routes.init_app(application,db)
    conf.init_app(application)
    return application

