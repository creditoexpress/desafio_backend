## BACKEND PROJECT:

Implementation of two APIs. First clientAPI checks whether a cliente is currently registered in the database. Second calcAPI returns a loan information rate request along with all the costs based on their credit score.

## Technology used:
Python - Django in backend


## USAGE:
- docker-compose up (to build the project)

## Testing Endpoint
localhost:8000
0.0.0.0:8000

## clienteAPI
Endpoint = http://127.0.0.1:8000/clientes/api/v1/

How it works:  
url = http://127.0.0.1:8000/clientes/api/v1/(cpf - celular)

example: http://127.0.0.1:8000/clientes/api/v1/01437256961-21981986733



## calcAPI
Endpoint = http://127.0.0.1:8000/taxas/api/v1/

How it works:  
url = http://127.0.0.1:8000/taxas/api/v1/(id)/(parcelas-valor)

example: http://127.0.0.1:8000/taxas/api/v1/50000/12-1000/



## Example code: 
mes = '12'  
valor = '10000'  
'http://127.0.0.1:8000/taxas/api/v1/' + id + '/' + mes + '-' + valor