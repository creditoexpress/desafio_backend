from mongoengine import Document, StringField

class Tipo_taxa( Document ):
    descr = StringField( required = True, unique = True )

#ATRIBUTOS JSON
JSON_TIPO = "tipo"
JSON_TAXAS = "taxas"

#TIPOS TAXA
class TipoTaxaEnum():
    NEGATIVADO = 'NEGATIVADO'
    SCORE_ALTO = 'SCORE_ALTO'
    SCORE_BAIXO = 'SCORE_BAIXO'
    VALOR_SCORE_ALTO = 500
