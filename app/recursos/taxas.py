import json
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from db.modelos.taxa import Taxa
from db.modelos.cliente import Cliente

class TaxaApi(Resource):
    def get(self):

        try:
            verify_jwt_in_request(True)
            cpf = get_jwt_identity()
            tipo = 'SCORE_BAIXO'

            print('cpf>>', cpf)

            if(cpf is not None):

                try:

                    cliente = Cliente.objects(cpf=str(cpf)).first().to_json()
                    cliente = json.loads(cliente)

                    print('cliente', cliente)
                    if(cliente["score"] > 500):
                        tipo = 'SCORE_ALTO'
                    
                    if(cliente["negativado"]):
                        tipo = 'NEGATIVADO'

                except Exception as e: 
                    print('Exception', e)
                    tipo = 'NEGATIVADO'

            else:
                tipo = 'NEGATIVADO'

            print('tipo>>', tipo)

            taxa = Taxa.objects.get(tipo=str(tipo)).to_json()
            taxa = json.loads(taxa)

            return Response(taxa["taxas"], mimetype="application/json", status=200)

        except Exception as e: 

            print('Exception', e)
            return Response(json.dumps({
                'erro': 'true',
                'mensagem': str(e)
            }), mimetype="application/json", status=500)