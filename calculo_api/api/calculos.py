from flask import request, jsonify
from flask_restful import Resource
import math

class CalculoApi(Resource):
    
    def get(self):

        request_data = request.args.to_dict()

        valor = request_data['valor']
        taxa = request_data['taxa']
        parcelas = request_data['parcelas']

        valor = float(valor)
        taxa = float(taxa)
        parcelas = float(parcelas)

        prestacao = valor*((taxa*(1+taxa)**parcelas)/(((1+taxa)**parcelas)-1))

        response = jsonify({
            'message': 'success',
            'valor_parcelas': round(prestacao, 2)
        })

        return response

