<h1 align="center">DESAFIO BACKEND</h1>

## Descrição do Projeto

Projeto criado para simular empréstimos através do score do cliente(NEGATIVADO, SCORE ALTO, SCORE BAIXO). Basta o cliente informar seu CPF e seu número de celular para se identificar. A simulação e realizada quando o cliente informa o valor do empréstimo e o número de parcelas desejados, podendo ser de 6, 12, 18, 24 ou 36.

## Tecnologia utilizada:

- Ruby on Rails

## Uso:

- docker-compose up web

## Endpoint clientes:

http://localhost:3000/clients/identify

- Exemplo: {
			"document": "123.123.123-12",
			"phone:""(34) 1231-1231"
			}

## Endpoint taxas:

http://localhost:3000/fees/simulat

- Exemplo: {
			"value": 1000,
			"plots": 36
			}