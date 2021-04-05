from mongoengine import BooleanField, Document, IntField, StringField


class Cliente(Document):

    nome = StringField(db_field='nome', required=True, max_length=255)
    cpf = StringField(db_field='cpf', required=True, max_length=11)
    celular = StringField(db_field='celular', required=True, max_length=11)
    score = IntField(db_field='score', required=True, min_value=0, max_value=1000)
    negativado = BooleanField(db_field='negativado', required=True)

    meta = {
            'collection': 'clientes',
            'db_alias': 'db',
            'max_documents': 200000000, 
            'max_size': 511000000
    }