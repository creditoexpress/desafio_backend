from mongoengine import Document, StringField, DictField

class Taxa(Document):
    tipo = StringField()
    taxas = DictField()