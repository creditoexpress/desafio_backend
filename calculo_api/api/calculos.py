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
            'valor_parcela': round(prestacao, 2)
        })

        return response


# >>> response = requests.get(request_url, request_body)
# >>> response
# <Response [200]>
# >>> response.content
# b'{\n  "message": "success", \n  "valor_parcela": 789.93\n}\n'
# >>> print(response.json())
# {'message': 'success', 'valor_parcela': 789.93}
# >>> 

# >>> request_body = {
# ...     "valor": 10000,
# ...     "taxa": 0.04,
# ...     "parcelas": 18
# ... }

# >> request_url = "http://127.0.0.1:5000/calculo"