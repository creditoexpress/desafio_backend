import json
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from db.modelos.taxa import Taxa
from db.modelos.cliente import Cliente

class CalculoApi(Resource):
    def post(self):

        try:
            body = request.get_json()

            if body is None:
                return Response(json.dumps({
                    'erro': 'true',
                    'mensagem': 'Informe o valor, o número de parcelas e a taxa de juros.'
                }), mimetype="application/json", status=500)

            print('body>>', body)

            if('numeroParcelas' in body and 'valor' in body and 'taxaJuros' in body):

                resp = dict()

                body["numeroParcelas"] = int(body["numeroParcelas"])
                body["taxaJuros"] = float(body["taxaJuros"])
                body["valor"] = float(body["valor"])

                resp["valorFinanciado"] = round(body["valor"] + (body["valor"] * body["taxaJuros"]), 2)
                resp["valorParcela"] = round(resp["valorFinanciado"] / body["numeroParcelas"], 2)

                return Response(json.dumps(resp), mimetype="application/json", status=200)

            else:
                return Response(json.dumps({
                    'erro': 'true',
                    'mensagem': 'Informe o valor, o número de parcelas e a taxa de juros.'
                }), mimetype="application/json", status=500)

        except Exception as e: 

            print('Exception', e)
            return Response(json.dumps({
                'erro': 'true',
                'mensagem': str(e)
            }), mimetype="application/json", status=500)