## Sobre a solução

Solução desenvolvida em python com Flask e mongodb. Aplicando conceitos SOLID e boas praticas de desenvolvimento para manter uma boa estrutura e um codigo limpo.
Além disso também aplicado alguns conceitos como Decorators, upload de arquivos, docker e ORM.

## Como Rodar

Para rodar subir a aplicação execute o seguinte comando na pasta raiz do projeto:
```shell
docker-compose up -d
```
Desta forma, estará rodando os container resposáveis pela API e pelo banco de dados da aplicação.
Obs: o banco de dados estará vazio e precisa ser preenchido.

# Utilizando
## Preenchendo o banco 
- Primeiramente é necessario preencher o banco de dados por meio dos arquivos fornecidos na pasta dados.
Para isso há duas rotas, uma para as taxas e outra para os usuarios.
### Usuarios
- Rota: [POST] http://0.0.0.0:3333/user/insert-file
- Inserir como corpo da requisição o arquivo "clientes.json" com o nome da key como "file"

### Taxas
- Rota: [POST] http://0.0.0.0:3333/taxa/insert-file
- Inserir como corpo da requisição o arquivo "taxas.json" com o nome da key como "file"

## Plano B
- Caso não obtenha sucesso em preencher o banco com os arquivos, também é possivel preenche-los informando o array de JSON manualmente no BODY da request. Da seguinte forma:
### Usuarios
- Rota: [POST] http://0.0.0.0:3333/user/insert
- Inserir como corpo da requisição o conteudo do arquivo "clientes.json".

### Taxas
- Rota: [POST] http://0.0.0.0:3333/taxa/insert
- Inserir como corpo da requisição o conteudo do arquivo "taxas.json".

## Rotas
- Algumas rotas possivéis da API

### Login
- Rota: [GET] http://0.0.0.0:3333/user/login
- Corpo: Informar no corpo da requisição um JSON contendo o **cpf** e o **celular** de algum usuario cadastrado anteriormente. Ex:
```javascript
{
    "cpf":"42935087160",
    "celular":"41996268329"
}
```
- Retorno: Retornará um Token JWT possibilitando a simulação de emprestimo.
- **Obs:** Caso não haja usuario cadastrado com esses dados será retornado Um Token JWT correspondente a um Usuario Visitante.

### Simular Emprestimo
- Rota: [GET] http://0.0.0.0:3333/simulacao_emprestimo/simular
- Header: Deve conter um Header **Authorization** contendo o Token JWT retornado na request de Login.
- Corpo:  Informar no corpo da requisição um JSON contendo o valores de **valor** e o **numeroParcelas** que serão usados pra simular o empréstimo. Ex:
```javascript
{
    "valor": 10000,
    "numeroParcelas": 12
}
``` 
- Retorno: Retornará um JSON contendo o resultado da simulaçao do Emprestimo. Ex:
```javascript
{
    "numeroParcelas": 12,
    "outrasTaxas": 85,
    "total": 10335.0,
    "valorJuros": 250.0,
    "valorParcela": 861.25,
    "valorSolicitado": 10000
}
```