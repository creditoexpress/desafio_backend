Passo a Passo para aplicação fora do Container

1- Criar um ambiente virtual
	python3 -m venv .venv

2- Ativar o ambiente virtual
	source .venv/bin/activate

3- Instalar as bibliotecas presentes no requirements.txt
	pip install -r requirements.txt

4- Criar um arquivo .env na raiz do projeto e inserir as variáveis de ambiente para executar o software localmente (Exemplo abaixo)

MONGODB_USERNAME=Seu_usuário_do_MongoDB
MONGODB_PASSWORD=Sua_senha_do_MongoDB

Não alterei as taxas de 18 parcelas tanto para SCORE_ALTO quando para SCORE_BAIXO, mas aparentemente estão erradas, marcando valores extremamente altos