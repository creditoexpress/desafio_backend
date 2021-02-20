from db.db import db

class Cliente(db.Document):
    nome = db.StringField(required=True)
    cpf = db.StringField(required=True)
    celular = db.StringField(required=True)
    score = db.LongField(required=True)
    negativado = db.BooleanField(required=True)