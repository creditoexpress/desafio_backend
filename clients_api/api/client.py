# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

# project resources
from models.clients import Clients


# @app.route('/clients/<cpf>&<cel>', methods=['GET'])
# def get_client(cpf, cel):
#     client = mongo.db.clients.find_one({'_cpf': cpf, '_cel': cel}) 
#     response = json_util.dumps(client)
#     return Response(response, mimetype='application/json')

class ClientsApi(Resource):
    def get(self):
        print('Aqui')
        # output = Clients.objects.get()
        print('Passou')
        return jsonify({'result': 'output'})

class ClientApi(Resource):
    
    def get(self):
        cpf = request.json['cpf']
        cel = request.json['cel']
        print(cpf)
        # output = Clients.objects.get(cpf=cpf, celular=cel)
        return jsonify({'result': 'output'})
