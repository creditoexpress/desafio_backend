## Executando o projeto

1. Clone este repositório;


1. Crie um volume local para o banco mongo:
        `$ docker volume create --name=mongodbdata`
1. Inicie os containers configurados:
        `docker-compose build && docker-compose up -d`
1. Crie o usuário para a aplicação no mongo:
      - `$ docker exec -it mongodb bash`
      - `$ mongo -u root -p`
      - `> use desafio_backend` 
      - `> db.createUser({user: 'desafio_backend', pwd: 'desafio_backend', roles: [{role: 'readWrite', db: 'desafio_backend'}]})`
      - `> exit`
1. Testando o novo usuário: 
      - `$ mongo -u desafio_backend -p desafio_backend --authenticationDatabase desafio_backend`
      - `> exit`


## Rotas

`GET http://localhost:3000/migracao`
- Obtém os dados dos JSON de cliente e taxas e insere no banco

`GET http://localhost:3000/cliente/:cpf/:celular`
- Retorna os dados e o token do cliente, que pode ser utilizado no serviço para buscar as taxas


`GET http://localhost:3000/taxa`
- Valida se existe token (Authorization Bearer) na requisição, caso exista, busca os dados do cliente, valida o score e se está negativado e retorna as taxas conforme, caso não exista o token, retorna as taxas para o tipo NEGATIVADO


`POST http://localhost:3000/calculo`
- JSON body: `{
	"numeroParcelas": 12,
	"valor": 10000,
	"taxaJuros": 0.04
}`
- Efetua o calculo e retorna o valor total e o valor da parecela
