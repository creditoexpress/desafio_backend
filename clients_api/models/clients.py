from mongoengine import Document, StringField, BooleanField, IntField

import re

class Clients(Document):
    nome = StringField(unique=False)
    cpf = IntField()
    celular = IntField()
    score = IntField()
    negativado = BooleanField()