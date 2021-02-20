from db.db import db

class Taxa(db.Document):
    tipo = db.StringField(required=True)
    taxas = db.StringField(required=True)