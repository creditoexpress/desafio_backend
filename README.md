# **Desafio Backend**
Neste arquivo encontra-se o modo de execução, da solução proposta para o [desafio](https://github.com/creditoexpress/desafio_backend)


### Executar
Iniciar docker
> docker-compose up -d --build

Executar shell para popular banco
> docker exec -it mongodb sh /bin/mongo-exec.sh

#### Para Criar usuário
1. > docker exec -it mongodb bash
2. > mongo -u credexpm -p 111222
3. > use desafio
4. > db.createUser({ user: "credexpf", pwd: "111222", roles: [ { role: "readWrite", db: "desafio" } ]})

<br/><br/>

##### Executar os testes
> docker exec -it api pytest tests/ -v --cov=src


<br/>


##### Consultar usuário
> curl --request GET --url http://127.0.0.1:4444/findClient?cpf=19867230540&&cel=31981648757  --header 'Content-Type: application/json'  

##### Simular empréstimo
> curl -v --request POST --cookie /tmp/exit   --url http://127.0.0.1:4444/simular   --header 'Content-Type: application/json'   --data '{ "numeroParcelas": 12,"valor": 10000}'

##### Ver qual usuário está simulando (para testes)
> curl --request GET --url http://127.0.0.1:4444/  --header 'Content-Type: application/json'  

<br/><br/><br/><br/>

### Requisitos
- Recomendo o uso de alguma ferramenta como Postman para testar as requisições, pois fazem controle de cookie.
- Deve-se iniciar o usuário no banco de dados.
- Será feita simulação no ultimo usuário consultado pelo 'findClient', caso não exista será feita simulação com um usuário de score 0.



