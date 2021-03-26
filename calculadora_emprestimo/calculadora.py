import requests
import os

def clear(): os.system('clear')

def main():

    while True:

        clear()

        while True:

            print("###############################################")
            print("########## Calculadora de Empréstimo ##########")
            print("###############################################")

            print("\n")

            print("ctrl+c para encerrar programa.")

            print("\n")

            # cpf_teste = "93762814031"
            # celular_teste = "71935228778"

            print("     Identifique-se")
            
            try:
                cpf = int(input(" CPF (Somente Números): "))
            except ValueError:
                print("\n Insira somente números")
                input("\n Press Enter to continue...")
                break
            try:
                celular = int(input(" Celular (Somente Números): "))
            except ValueError:
                print("\n Insira somente números")
                input("\n Press Enter to continue...")
                break

            # request_url = "http://127.0.0.1:5002/client"
            request_url = "http://0.0.0.0:5002/client"
            request_body = {
                "cpf": cpf,
                "celular": celular
            }

            response = requests.get(request_url, request_body)

            response_data = response.json()

            status_client = response_data['status']
            if status_client == 404:
                message_client = response_data['message']
                print(message_client + '\n')
                input('Press Enter to continue...')

                break

            nome = response_data["nome"]
            cpf = response_data["cpf"]
            celular = response_data["celular"]
            score = response_data["score"]
            negativado = response_data["negativado"]

            try:
                valor_financiado = float(input(" Valor desejado (\" . \" para ponto flutuante): "))
            except ValueError:
                print("\n Insira somente números, e \" . \" para ponto flutuante.")
                input("\n Press Enter to continue...")
                break
            finally:
                if valor_financiado <= 0:
                    print("\n Insira somente valor positivo")
                    input("\n Press Enter to continue...")
                    break
            while True:
                choices = [6, 12, 18, 24, 36]
                parcelas = int(input(" Nº de Parcelas (opções: 6, 12, 18, 24 ou 36): "))
                if parcelas not in choices:
                    print('Numero de parcelas inválido. Insira novamente.')
                else:
                    break

            request_url = "http://0.0.0.0:5003/taxa"
            request_body = {
                "score": score,
                "negativado": negativado,
                "parcelas": parcelas
            }

            response = requests.get(request_url, request_body)
            response_data = response.json()

            taxa = response_data["taxa"]

            request_url = "http://0.0.0.0:5004/calculo"
            request_body = {
                "valor": valor_financiado,
                "taxa": taxa,
                "parcelas": parcelas
            }

            response = requests.get(request_url, request_body)
            response_data = response.json()

            valor_parcelas = response_data["valor_parcelas"]

            clear()

            print("###############################################")
            print("################## Simulação ##################")
            print("###############################################")
            print('\n')
            print("Nome: " + nome)
            print("Nº de parcelas: ", parcelas)
            print("Taxa de juros: ", taxa*100, "%")
            print("Valor financiado: ", valor_financiado)
            print("Valor da prestação: ", valor_parcelas)
            print("\n\n")
            input("Para fazer nova simulação, pressione enter... \nPara encerrar o programa ctrl+c.")
            break

if __name__ == "__main__":
    main()