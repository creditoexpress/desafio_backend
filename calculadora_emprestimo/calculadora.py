import requests

def main():
    print("###############################################")
    print("########## Calculadora de Empréstimo ##########")
    print("###############################################")

    print("\n\n")

    cpf_teste = "93762814031"
    celular_teste = "71935228778"

    print("     Identifique-se")
    cpf = input(" CPF: ")
    celular = input(" CELULAR: ")

    request_url = "http://127.0.0.1:5002/client"
    request_body = {
        "cpf": cpf_teste,
        "celular": celular_teste
    }

    response = requests.get(request_url, request_body)
    print(response)
    response_data = response.json()

    nome = response_data["nome"]
    cpf = response_data["cpf"]
    celular = response_data["celular"]
    score = response_data["score"]
    negativado = response_data["negativado"]

    valor_teste = 10000
    parcelas_teste = 18

    valor = input(" Valor desejado: ")
    parcelas = input(" Nº de Parcelas (6, 12, 18, 24 ou 36): ")

    request_url = "http://127.0.0.1:5003/taxa"
    request_body = {
        "score": score,
        "negativado": negativado,
        "parcelas": parcelas_teste
    }

    response = requests.get(request_url, request_body)
    response_data = response.json()

    taxa = response_data["taxa"]
    print("taxa = ", taxa)

    request_url = "http://127.0.0.1:5004/calculo"
    request_body = {
        "valor": valor_teste,
        "taxa": taxa,
        "parcelas": parcelas_teste
    }

    response = requests.get(request_url, request_body)
    response_data = response.json()

    valor_parcelas = response_data["valor_parcelas"]
    print(valor_parcelas)


if __name__ == "__main__":
    main()