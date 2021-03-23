import requests, json, logging

def calular_emprestimo_request( emprestimo, taxa_juros ):
    request_data = {
        "numeroParcelas": emprestimo.num_parcelas,
	    "valor": emprestimo.val_emprestimo,
	    "taxaJuros": taxa_juros
    }
    
    logging.info( "[REQUEST_BODY] << {}".format( request_data ) )

    url = "https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend"
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers = headers, data = json.dumps( request_data ) )

    return response.json()