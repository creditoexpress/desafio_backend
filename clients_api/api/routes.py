from flask_restful import Api

from api.client import ClientsApi, ClientApi

def create_routes(api: Api):

    api.add_resource(ClientApi, '/client')
    api.add_resource(ClientsApi, '/clients')