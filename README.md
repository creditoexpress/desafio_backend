## BACKEND PROJECT:

Implamentation of two APIs. First clientAPI, check whether a cliente is currently register in the database. Second calcAPI returns a loan information rate along with the costs, based on their credit score.

## Technology used:
Python - Django in backend


## USAGE:
- docker-compose up (to build the project)

## Testing Endpoint
localhost:8000
0.0.0.0:8000

## clienteAPI
url = http://127.0.0.1:8000/clientes/api/v1/(cpf - celular)

exemplo: http://127.0.0.1:8000/clientes/api/v1/01437256961-21981986733



## calcAPI

url = http://127.0.0.1:8000/taxas/api/v1/(id)/(parcelas-valor)

exemplo: http://127.0.0.1:8000/taxas/api/v1/50000/12-1000/

code ex: 
mes = '12'
valor = '10000'
'http://127.0.0.1:8000/taxas/api/v1/' + id + '/' + mes + '-' + valor