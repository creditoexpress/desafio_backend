import json
import datetime
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from db.modelos.cliente import Cliente

class ClienteApi(Resource):
    def get(self, cpf, celular):

        try:

            cliente = Cliente.objects(cpf=str(cpf), celular=str(celular)).first().to_json()
            cliente = json.loads(cliente)
            expires = datetime.timedelta(days=1)
            cliente["access_token"] = create_access_token(identity=str(cliente["cpf"]), expires_delta=expires)
            return Response(json.dumps(cliente), mimetype="application/json", status=200)

        except Exception as e: 

            print('Exception', e)
            return Response(json.dumps({
                'erro': 'true',
                'mensagem': 'Cliente não encontrado'
            }), mimetype="application/json", status=404)