from mongoengine import Document, StringField, BooleanField, IntField

class User( Document ):
    nome = StringField( required = True )
    cpf = StringField( required = True, max_length = 11 )
    celular = StringField(  required = True, max_length = 11 )
    score = IntField( required = True )
    negativado = BooleanField( required = True, default = False)

    def __str__( self ):
        return """Nome: {nome},
                  CPF: {cpf},
                  Celular: {celular},
                  Score: {score},
                  Negativado: {negativado}
        """.format( nome=self.nome, 
                    cpf=self.cpf, 
                    celular=self.celular, 
                    score=self.score, 
                    negativado=self.negativado )

#Atributos
NOME = 'nome'
CPF = 'cpf'
CELULAR = 'celular'
SCORE = 'score'
NEGATIVADO = 'negativado'

#ENUM TIPO USUARIO
VISITANTE = 0