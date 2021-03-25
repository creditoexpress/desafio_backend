# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

from bson import json_util

# project resources
from models.clients import Client


class ClientsApi(Resource):
    def get(self):
        clients = Client.objects().fields(id=0).as_pymongo()

        clients_dumps = json_util.dumps(clients)

        return Response(clients_dumps, mimetype='application/json')

class ClientApi(Resource):
    
    def get(self):
        cpf = request.json['cpf']
        cel = request.json['cel']

        client = Client.objects.get(cpf=cpf, celular=cel)

        client_data = client._data

        client_data.pop('id')

        client_dumps = json_util.dumps(client_data)

        return Response(client_dumps, mimetype='application/json')

