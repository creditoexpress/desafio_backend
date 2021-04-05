from mongoengine import DictField, Document, StringField


class Taxa(Document):
    
    tipo = StringField(db_field='tipo', required=True, max_length=11, unique=True)
    taxas = DictField(db_field='taxas', required=True)

    meta = {
            'collection': 'taxas',
            'db_alias': 'db',
            'max_documents': 1000, 
            'max_size': 1000000
    }