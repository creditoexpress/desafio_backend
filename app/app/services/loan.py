from json import loads
from requests import post

from app.services.database import Database


class Loan:

    @staticmethod
    def simulate(request_data, decode):
        db = Database()
        
        cliente = db.select_cliente(decode['cpf'], decode['celular'])

        parcelas = request_data['numeroParcelas']

        if cliente:
            cliente = cliente[0]
            score = cliente.score
            negativado = cliente.negativado
        else:
            score = 0
            negativado = False

        if negativado:
            taxa = db.select_taxa('NEGATIVADO')
            taxa_juros = taxa[0].taxas[str(parcelas)]
            request_data['taxaJuros'] = taxa_juros
        elif score <= 500:
            taxa = db.select_taxa('SCORE_BAIXO')
            taxa_juros = taxa[0].taxas[str(parcelas)]
            request_data['taxaJuros'] = taxa_juros
        elif score > 500:
            taxa = db.select_taxa('SCORE_ALTO')
            taxa_juros = taxa[0].taxas[str(parcelas)]
            request_data['taxaJuros'] = taxa_juros

        response = Loan.calculate_api(request_data)
        response_json = loads(response.text)

        return response_json

    @staticmethod
    def calculate_api(payload):

        url = 'https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend'
        headers = {'Content-Type': 'application/json'}
        response = post(url, headers=headers, json=payload)

        return response