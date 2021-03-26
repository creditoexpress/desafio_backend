## Sobre a Crédito Express

A Crédito Express é uma fintech voltada para servir instituições financeiras. Nosso objetivo é levar TAXAS ATRATIVAS para as pessoas, a partir do uso de tecnologia de ponta.

VENHA FAZER PARTE DESSA REVOLUÇÃO FINANCEIRA!


## Sobre o desafio

Com o aumento dos casos de COVID-19 muitos cidadãos tiveram aumentos nos gastos e redução nos ganhos, levando a eles endividarem-se em meios que as taxas de juros são extremamente altas. Neste desafio você deve construir uma aplicação para pessoas possam simular empréstimos com as melhores taxas do mercado financeiro.

A aplicação deve ter uma API para o cliente informar o seu CPF e numero de celular para se identificar e depois disso ele poderá efetuar simulações de empréstimo em outra API. Para simular é necessário informar o valor do empréstimo e o número de parcelas, sendo que podem ser 6, 12, 18, 24 ou 36.

Existe uma tabela de taxas, o calculo do empréstimo deve ser feito de acordo com ela. Existem 3 tipos diferentes de taxas: **negativado, score alto e score baixo**. Pessoas com score acima de 500 são consideradas com score alto nessa aplicação, pessoas sem cadastro na base recebem score 0.

Após obter o valor da taxa a ser aplicada para esse cliente, será necessário chamar uma API para fazer o cálculo da simulação. Os dados retornados pelo cálculo devem ser o retorno da sua API.


## Considerações

- O arquivo taxas.json possui uma coleção de taxas por característica. Os dados seguem o formato do exemplo abaixo, mas pode modificar a estrutura no seu projeto se precisar:

```javascript
  {
	"tipo": "NEGATIVADO",
	"taxas": {"6": 0.04, "12": 0.045, "18": 0.05, "24": 0.053, "36": 0.055}
  }
```
- O arquivo clientes.json possui uma coleção de objetos que representam os clientes que já tem pré-cadastro. Abaixo temos um exemplo do formato do objeto que também pode ter a estrutura modificada caso julgue necessário.

```javascript
{
	"nome": "Roberto Filipe Figueiredo",
	"cpf": "41882728564",
	"celular": "6526332774",
	"score": 300,
	"negativado": false
}
```

- Abaixo temos um exemplo de um CURL para API de cálculo.

```shell
curl --request POST \
  --url https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend \
  --header 'Content-Type: application/json' \
  --data '{
	"numeroParcelas": 12,
	"valor": 10000,
	"taxaJuros": 0.04
}'
```

### Pré-requisitos
- Desenvolvimento de API REST em Python;
- Utilização do MongoDB;
- Desenvolvimento de um Dockerfile/Docker-Compose.yml para rodar o projeto;
- Documentar como rodamos o projeto no README.MD;

### Diferenciais/Extras
- Implementação de Testes de unidade e/ou integração;
- Clean code;
- Segurança e resiliência;
- Utilização de padrões de projeto;
- Migrations e/ou seeders;
- Script para execução da aplicação;

## Pronto para começar o desafio?

- Faça um "fork" deste repositório na sua conta do Github;
- Após completar o desafio, crie um pull request nesse repositório comparando a sua branch com a master com o seu nome no título;

## Helps
- https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/

FROM python:latest

WORKDIR /usr/src/clients_app

COPY requirements.txt ./

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

COPY . .

CMD "python3 app.py"



# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5002

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "python3", "app:app", "--host=0.0.0.0:5002"]


COMPOSE

version: "3.8"

services: 
  web_client:
    build: "./clients_api"
    ports:
      - "5002:5002"
    links:
      - desafio_bd
  web_taxa:
    build: "./taxas_api"
    ports:
      - "5003:5003"
    links:
      - desafio_bd
  web_calculo:
    build: "./calculo_api"
    ports:
      - "5004:5004"
    links:
      - desafio_bd
  desafio_bd:
    image: mongo:latest
    hostname: mongodb
    ports:
      - '27018:27018'



  volumes:
    ./init-fb.js/docker-entrypoint-initdb.d/init-db.js:ro