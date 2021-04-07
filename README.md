
# API para simulação de empréstimo

## Para o projeto foi utilizado:
- Docker/docker-compose - virtualização de containeres
- python3.8-slim/flask - linguagem base e micro-framework para desenvolvimento de web API
- pkosiec/mongo-seeding:3.6.0 - ferramenta de importação automatica de dados para mongodb
- Mongodb Atlas Cloud Database - versão cloud do Mongodb

## Execução

- Para subir o projeto, navegue até seu diretório e execute o seguinte comando
```shell
docker-compose up -d
```
*obs.: remova o **-d** caso queira ver os logs*
- Automaticamente serão executados os *seeds* para clientes e taxas, sempre que precisar dar re-build todas as collections serão deletadas e os *seeds* inseridos novamente


## Endpoints

|Tipo|Endpoint|Método|Campos|Requer Autenticação|
|--|--|--|--|--|
|Clientes|localhost:5000/clients/|POST|nome (string), cpf (string), celular (string)|Não|
|Autenticação|localhost:5000/clients/auth|POST|cpf (string), celular (string)|Não|
|Simulação|localhost:5000/loans/|POST|cpf (string), numeroParcelas (int), valor (decimal)|Sim|



## Exemplos

 - **Clientes**
 -> Exemplo de *body* para cadastro de um cliente:

       {
	    	"nome": "Fábio Erickson",
	    	"cpf": "72168204012",
			"celular": "34999999999"
       }
	
	O retorno será o status do cadastramento.

 - **Autenticação**
 -> Exemplo de *body* para autenticação de um cliente:

       {
	    	"cpf": "93762814031",
			"celular": "71935228778"
       }
	O retorno deverá ser:

       {
	    	"status": "Cliente autorizado",
			"token": "Bearer eyJ0eXAiOiJKV1QiLCzUxMiJ9...7QAyz3A"
       }

 - **Simulação**
 -> Exemplo de *body* para simulação de empréstimo:

	    {
		    "cpf": "93762814031",
		    "numeroParcelas": 12,
		    "valor": 10000
	    }
	O retorno deverá ser:
		

		{
			"numeroParcelas": 12,
			"outrasTaxas": 85,
    		"total": 10535.0,
    		"valorJuros": 450.0,
    		"valorParcela": 877.92,
    		"valorSolicitado": 10000
	   }

## Testes

- **Requerimentos**
-> É necessário ter instalados o *python* e as biblioteca *pytest* e *flask*:
```shell
sudo apt install python3.8
sudo apt install python3-pip
pip3 install pytest
pip3 install flask
```
- **Comando**
-> Para realizar os testes execute o seguinte comando no terminal:
```shell
pytest -c pytest.ini
```
- Os logs do progresso de teste serão printados no console