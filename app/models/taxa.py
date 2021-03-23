from mongoengine import Document, IntField, FloatField, ReferenceField, CASCADE

from .tipo_taxa import Tipo_taxa

class Taxa( Document ):
    num_parcelas = IntField( required = True, max_value = 36, min_value = 6 )
    juros = FloatField( required = True, max_value = 1, min_value = 0 )
    id_tipo_taxa = ReferenceField( Tipo_taxa, reverse_delete_rule = CASCADE )

NUM_PARCELAS = 'num_parcelas'
JUROS = 'juros'
ID_TIPO_TAXA = 'id_tipo_taxa'