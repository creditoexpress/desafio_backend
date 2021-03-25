# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

from bson import json_util

# project resources
from models.taxas import Taxa


class TaxasApi(Resource):
    def get(self):
        taxas = Taxa.objects().fields(id=0).as_pymongo()

        taxas_dumps = json_util.dumps(taxas)

        return Response(taxas_dumps, mimetype='application/json')

class TaxaApi(Resource):
    
    def get(self):
        score = request.json['score']
        negativado = request.json['negativado']
        parcela = request.json['parcela']

        if negativado:
            tipo = "NEGATIVADO"
        else:
            if score > 500:
                tipo = "SCORE_ALTO"
            else:
                tipo = "SCORE_BAIXO"

        taxa = Taxa.objects.get(tipo=tipo)

        taxa_data = taxa._data

        taxa = taxa_data['taxas'].pop(parcela)

        response = jsonify({
            'message': 'success',
            'taxa': taxa
        })

        return response