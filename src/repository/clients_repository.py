from src.setup.database import Database
from src.model import Client

class ClientsRepository:
    
    def __init__(self):
        self.db = Database()
        
    def create_client(self, body):
        self.db.connect_db()
        client = Client.objects.insert(doc_or_docs=body)
        self.db.disconnect_db()
        return client['id']
    
    def exists_client(self, CPF):
        self.db.connect_db()
        exists = True
        client = None
        try:
            client = Client.objects.get(cpf=CPF)
            if client is None:
                exists = False
        except:
            exists = False
        self.db.disconnect_db()
        return exists
  
    def get_client_by_cpf(self, CPF):
        self.db.connect_db()
        client = None
        try:
            client = Client.objects.get(cpf=CPF)
        except:
            client = None
        self.db.disconnect_db()
        return client
        
        