from mongoengine import Document, StringField, BooleanField, IntField

class Client(Document):

    ### Client(nome="Marcelo", cpf="12225832757", celular="27997771850", score=550, negativado=True)

    nome = StringField(unique=False)
    cpf = IntField()
    celular = IntField()
    score = IntField()
    negativado = BooleanField()

    meta = {
        'ordering': ['nome']
    }