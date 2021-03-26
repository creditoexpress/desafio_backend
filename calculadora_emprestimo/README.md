## Execução - Necessário ter API's Listening para usar a calculadora.

1- Abrir o bash no diretório raiz "calculadora_emprestimo", criar um ambiente virtual de desenvolvimento (venv), ativá-lo e instalar as bibliotecas presentes no requirements.txt
    - Caso não tenha instalado o virtualenv, instale-o via pip
        - $ pip install virtualenv
    - Abra o bash no diretório "/desafio_backend/calculadora_emprestimo"
    - Crie o ambiente virtual de desenvolvimento
        - $ python3 -m venv .venv
    - Ative o ambiente virtual
        - $ source .venv/bin/activate (linux ou macOS)
        - $ .venv/Script/activate (Windows)
    - Instale as bibliotecas no venv
        - $ pip install -r requirements.txt
        
2- Executar a calculadora de empréstimo
    - python3 calculadora.py