from mongoengine import Document, StringField, IntField, BooleanField

class Client(Document):
    nome = StringField(max_length=255, required=True)
    celular = StringField(max_length=20, required=True)
    cpf = StringField(max_length=11, required=True)
    score = IntField()
    negativado = BooleanField()

    meta = { 'collection': 'clientes', 'db_alias': 'mongocloud' }