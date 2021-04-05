from mongoengine import connect, disconnect

from application.models.cliente import Cliente
from application.models.taxa import Taxa


class Database:

    def __init__(self):
        self.host = 'mongodb+srv://chrysrodev:Rcg9NIXW5QlfEmOV@cluster-aurora.1xpil.mongodb.net/creditExpress?retryWrites=true&w=majority'
        self.alias = 'db'
        self.db = 'creditExpress'

    def open_connection(self):
        connect(host=self.host, alias=self.alias, db=self.db)
    
    def close_connection(self):
        disconnect(alias=self.alias)

    def insert_clientes(self, documents):
        self.open_connection()
        
        objects_ids =  Cliente.objects.insert(doc_or_docs=documents, load_bulk=False, write_concern={'w': 3, 'fsync': True})

        self.close_connection()

        return objects_ids

    def select_cliente(self, cpf, celular):
        self.open_connection()
        
        cliente =  Cliente.objects(cpf=cpf, celular=celular)

        self.close_connection()

        return cliente

    def insert_taxas(self, documents):
        self.open_connection()
        
        objects_ids =  Taxa.objects.insert(doc_or_docs=documents, load_bulk=False, write_concern={'w': 3, 'fsync': True})

        self.close_connection()

        return objects_ids

    def select_taxa(self, tipo):
        self.open_connection()
        
        taxa =  Taxa.objects(tipo=tipo)

        self.close_connection()

        return taxa