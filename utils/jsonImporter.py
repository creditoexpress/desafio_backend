import json


def importarClientes():
    queryset = Clientes.objects.all()
    with open('clientes.json') as json_file:
        data = json.loads(json_file.read())
        for cliente in data:
            if not cliente['cpf'] in queryset:
                Clientes.objects.create(
                    nome=cliente['nome'],
                    cpf=cliente['cpf'],
                    celular=cliente['celular'],
                    score=cliente['score'],
                    negativado=cliente['negativado']
                )
