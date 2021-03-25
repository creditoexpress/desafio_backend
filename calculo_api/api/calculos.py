from flask import request, jsonify
from flask_restful import Resource
import math

class CalculoApi(Resource):
    
    def get(self):
        valor = request.json['valor']
        taxa = request.json['taxa']
        parcelas = request.json['parcelas']

        valor = float(valor)
        taxa = float(taxa)

        prestacao = valor*((taxa*(1+taxa)**parcelas)/(((1+taxa)**parcelas)-1))

        response = jsonify({
            'message': 'success',
            'valor_parcela': round(prestacao, 2)
        })

        return response