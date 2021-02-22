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