class ClientsRepository:
    def __init__(self, collection) -> None:
        self.clients = collection

    def find_by_cpf(self, cpf: str):
        return self.clients.find_one({ 'cpf': cpf })
