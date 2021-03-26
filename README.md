# O que essa API faz?

Essa API implementa uma solução de consulta de empréstimos com as melhores taxas do mercado financeiro. A consulta é feita à uma API externa que retorna todos os dados do empréstimo, como a seguir:

```json
{
  "numeroParcelas": 6,
  "outrasTaxas": 85,
  "total": 1130,
  "valorJuros": 45,
  "valorParcela": 188.33,
  "valorSolicitado": 1000
}
```

# Como executar esse projeto

- Clone o projeto;
- Execute o comando **yarn** para instalação de todas as dependências desse projeto;
- Para configurar o banco de dados de forma prática, execute o comando **docker-compose up -d**. Será criada uma imagem do MongoDB;
- Crie uma chave secreta para que o token gerado seja validado e insira na variável ambiente APP_SECRET;
- Preencha a variável ambiente SERVER_PORT com a porta em que o servidor irá rodar;
- As variáveis DB_HOST, DB_PORT e DB_NAME deixei preenchidas com as configurações que utilizei nesse projeto;
- Após esses procedimentos, rode o comando **yarn dev** (script configurado no package.json). Caso esteja tudo ok, a mensagem **🚀 Executando na porta PORT** deve aparecer no console.

# Rotas e recursos

- Para conseguir ter acesso a todos os recursos, acesse as rotas do projeto. Elas estão litadas logo abaixo:

**POST**: **'/register'** 
- Rota para cadastro de um usuário. Se os dados forem inseridos corretamente, seu retorno será algo como (é importante inserir um cpf válido. Para esse exemplo foi utilizado um cpf fake):

* Dados que devem ser inseridos:

```json
{
	"name": "Albert",
	"email": "albert@mail.com",
	"cpf": "33992127044",
	"cellPhone": 9999999
}
```
* O retorno dessa rota:

```json
{
  "register": {
    "name": "Albert",
    "email": "albert@mail.com",
    "cellPhone": 9999999,
    "score": 550,
    "negative": false,
    "created_at": "2021-03-24T18:50:47.692Z",
    "updated_at": "2021-03-24T18:50:47.692Z",
    "id": "605b8a07305d2513b5fb0061"
  }
}
```

**POST** - **'/session'** 
- Rota para gerar uma sessão para o usuário. É importante ressaltar que, para gerar uma sessão válida, não há a necessidade de se criar um registro antes. Caso o usuário não seja cadastrado na aplicação, ele poderá realizar a consulta de empréstimo normalmente, porém, atendendo os requisitos de baixo score (o cpf aqui também deve ser válido).

* Dados que devem ser inseridos nessa rota:

```json
{
	"email": "albert@mail.com",
	"cpf": "33992127044",
	"cellPhone": 99999	
}
```
* O retorno dessa rota:

```json
{
  "session": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29yZSI6NTUwLCJuZWdhdGl2ZSI6ZmFsc2UsImVtYWlsIjoiYWxiZXJ0QG1haWwuY29tIiwiaWF0IjoxNjE2NjEyOTA0LCJleHAiOjE2MTY2MTY1MDQsInN1YiI6IiQyYiQxMCRERmNjLzhEaVJYcXVOMVlxZ0hURXNPeVlwOHNacC45LlF6eGxEaFF5OXh2Ty4wYUUwcTd5ZSJ9.E11LwZvopgPILB_lv8VdlmBUgSX0YpFCUd6_GvSkpZ4",
    "user": {
      "id": "605b8a07305d2513b5fb0061",
      "name": "Albert",
      "email": "albert@mail.com",
      "cellPhone": 9999999,
      "score": 550,
      "negative": false,
      "created_at": "2021-03-24T18:50:47.692Z",
      "updated_at": "2021-03-24T18:50:47.692Z"
    }
  }
}
```

**POST** - **'/loan'**
- Rota responsável por fazer a consulta para a API de cálculo de empréstimo. Para que seja possível realizar uma consulta corretamente, as taxas e parcelas precisam estar cadastradas, conforme explicado posteriormente. Para esse projeto não implementei a funcionalidade de seeds.

- **O token gerado na sessão precisa ser fornecido para essa rota**.

* Dados que devem ser inseridos nessa rota:

```json
{
	"installments": 6,
	"value": 1000
}
```

* O retorno dessa rota:

```json
{
  "numeroParcelas": 6,
  "outrasTaxas": 85,
  "total": 1130,
  "valorJuros": 45,
  "valorParcela": 188.33,
  "valorSolicitado": 1000
}
```

**POST** - **'/rates'**
- Essa rota é responsável pelo cadastro do tipo, da parcela e a taxa relacionada à essa parcela. Os tipos válidos são: SCORE_BAIXO E SCORE_ALTO. Para usuários negativados, a consulta não será permitida. Caso algum outro tipo seja cadastrado, a API retornará um erro 400.

* Dados que devem ser inseridos nessa rota:

```json
{
	"type": "SCORE_BAIXO",
	"installments": 12,
	"rate": 0.045
}
```

* O retorno dessa rota:

```json
{
  "type": "SCORE_BAIXO",
  "installments": 12,
  "rate": 0.045,
  "created_at": "2021-03-24T18:29:05.010Z",
  "updated_at": "2021-03-24T18:29:05.010Z",
  "id": "605b84f11ee8b512fc18e2cb"
}
```

# Rodar os testes

- Para rodar os testes, basta executar o comando **yarn test** no console. Uma informação importante é que, nesse projeto não consegui implementar o MongoDB em memória junto ao TypeORM. Dessa forma, nos testes de integração é utilizado o banco local para realizar a inserção e deleção dos dados. 

- No arquivo RegisterAccountRepository.spec.ts, em src/modules/users/infra/typeorm/repositories/implementations, também utiliza o banco local para os testes.

## Estrutura de pastas do projeto

```
📦src
 ┣ 📂@types
 ┃ ┗ 📜express.d.ts
 ┣ 📂__test__
 ┃ ┣ 📜consultSession.spec.ts
 ┃ ┗ 📜register.spec.ts
 ┣ 📂config
 ┃ ┗ 📜auth.ts
 ┣ 📂modules
 ┃ ┗ 📂users
 ┃ ┃ ┣ 📂dtos
 ┃ ┃ ┃ ┣ 📜ICreateInstallmentsDTO.ts
 ┃ ┃ ┃ ┣ 📜IRegisterAccountDTO.ts
 ┃ ┃ ┃ ┗ 📜InterestRateDTO.ts
 ┃ ┃ ┣ 📂infra
 ┃ ┃ ┃ ┣ 📂http
 ┃ ┃ ┃ ┃ ┗ 📂controllers
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ConsultSessionController.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜LoanSimulationController.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜RatesRegistrationController.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜RegisterController.ts
 ┃ ┃ ┃ ┗ 📂typeorm
 ┃ ┃ ┃ ┃ ┣ 📂repositories
 ┃ ┃ ┃ ┃ ┃ ┣ 📂implementations
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜InterestRateRepository.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RegisterAccountRepository.spec.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜RegisterAccountRepository.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📂protocol
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜IInterestRateRepository.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜IRegisterAccountRepository.ts
 ┃ ┃ ┃ ┃ ┣ 📂schema
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Account.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜Rate.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┃ ┃ ┣ 📂routes
 ┃ ┃ ┃ ┣ 📜consultSession.routes.ts
 ┃ ┃ ┃ ┣ 📜loanSimulation.routes.ts
 ┃ ┃ ┃ ┣ 📜ratesRegistration.routes.ts
 ┃ ┃ ┃ ┗ 📜register.routes.ts
 ┃ ┃ ┗ 📂useCases
 ┃ ┃ ┃ ┣ 📂ConsultSession
 ┃ ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┃ ┗ 📜IConsultSessionUseCase.ts
 ┃ ┃ ┃ ┃ ┣ 📜ConsultSessionUseCase.spec.ts
 ┃ ┃ ┃ ┃ ┣ 📜ConsultSessionUseCase.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┃ ┃ ┃ ┣ 📂CreateUser
 ┃ ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┃ ┗ 📜IRegisterUseCase.ts
 ┃ ┃ ┃ ┃ ┣ 📜RegisterUseCase.spec.ts
 ┃ ┃ ┃ ┃ ┣ 📜RegisterUseCase.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┃ ┃ ┃ ┣ 📂LoanSimulation
 ┃ ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ILoanSimulationUseCase.ts
 ┃ ┃ ┃ ┃ ┣ 📜LoanSimulationUseCase.spec.ts
 ┃ ┃ ┃ ┃ ┣ 📜LoanSimulationUseCase.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┃ ┃ ┃ ┗ 📂RatesRegistration
 ┃ ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┃ ┗ 📜IRatesRegistrationUseCase.ts
 ┃ ┃ ┃ ┃ ┣ 📜RatesRegistrationUseCase.spec.ts
 ┃ ┃ ┃ ┃ ┣ 📜RatesRegistrationUseCase.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┗ 📂shared
 ┃ ┣ 📂errors
 ┃ ┃ ┣ 📜AppError.ts
 ┃ ┃ ┣ 📜ClientRequestError.ts
 ┃ ┃ ┗ 📜InternalError.ts
 ┃ ┣ 📂infra
 ┃ ┃ ┗ 📂http
 ┃ ┃ ┃ ┣ 📂config
 ┃ ┃ ┃ ┃ ┣ 📜app.ts
 ┃ ┃ ┃ ┃ ┗ 📜middlewares.ts
 ┃ ┃ ┃ ┣ 📂middlewares
 ┃ ┃ ┃ ┃ ┗ 📜confirmUserAuthenticated.ts
 ┃ ┃ ┃ ┣ 📂routes
 ┃ ┃ ┃ ┃ ┗ 📜index.ts
 ┃ ┃ ┃ ┗ 📜server.ts
 ┃ ┗ 📂providers
 ┃ ┃ ┣ 📂AxiosProvider
 ┃ ┃ ┃ ┣ 📂protocol
 ┃ ┃ ┃ ┃ ┗ 📜IRequestProvider.ts
 ┃ ┃ ┃ ┗ 📜RequestProvider.ts
 ┃ ┃ ┣ 📂ClassTransformerProvider
 ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┗ 📜ITransformerProvider.ts
 ┃ ┃ ┃ ┗ 📜ClassTransformerProvider.ts
 ┃ ┃ ┣ 📂CpfValidator
 ┃ ┃ ┃ ┣ 📂protocol
 ┃ ┃ ┃ ┃ ┗ 📜ICpfValidatorProvider.ts
 ┃ ┃ ┃ ┗ 📜CpfValidatorProvider.ts
 ┃ ┃ ┣ 📂ExpressProvider
 ┃ ┃ ┃ ┣ 📂protocol
 ┃ ┃ ┃ ┃ ┗ 📜IHttpRequest.ts
 ┃ ┃ ┃ ┗ 📜HttpRequest.ts
 ┃ ┃ ┣ 📂HashProvider
 ┃ ┃ ┃ ┣ 📂protocol
 ┃ ┃ ┃ ┃ ┗ 📜IHashProvider.ts
 ┃ ┃ ┃ ┗ 📜BCryptHashProvider.ts
 ┃ ┃ ┗ 📂TokenManager
 ┃ ┃ ┃ ┣ 📂protocol
 ┃ ┃ ┃ ┃ ┗ 📜ITokenManagerProvider.ts
 ┃ ┃ ┃ ┗ 📜TokenManagerProvider.ts
```