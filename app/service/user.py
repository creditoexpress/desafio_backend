import logging

from repository import user as user_repository

from models.user import *
from models.tipo_taxa import TipoTaxaEnum

def insert_users( users ):
    users_response = list()
    
    for user in users:
        try:
            user = refactor_user_atributes( user )

            user_response = user_repository.insert_user( user )
            users_response.append( user_response )
            
        except Exception as e:
            raise Exception( "[ERROR] << {}\n[USER] << {}".format( e, user ) )

    return users_response

def find_user_by_cpf_and_cellphone( cpf, cellphone ):
    user = user_repository.find_user_by_cpf_and_cellphone( cpf, cellphone )
    logging.info( "USER << {}".format( user if user else "Not Found" ) )
    return user

def refactor_user_atributes( user ):
    user[ NOME ] = str( user[ NOME ] )
    user[ CPF ] = str( user[ CPF ] )
    user[ CELULAR ] = str( user[ CELULAR ] )
    user[ SCORE ] = int( user[ SCORE ] )
    user[ NEGATIVADO ] = bool( user[ NEGATIVADO ] )
    return user

def get_tipo_taxa_user_by_user_id( user_id ):
    if user_id == VISITANTE:
        return validate_tipo_taxa( 0, False )
        
    user = user_repository.find_user_by_id( user_id )

    tipo_taxa = validate_tipo_taxa( user.score, user.negativado )

    return tipo_taxa

def validate_tipo_taxa( score, negativado ):
    if negativado:
        return TipoTaxaEnum.NEGATIVADO
    
    if score > TipoTaxaEnum.VALOR_SCORE_ALTO:
        return TipoTaxaEnum.SCORE_ALTO
    else:
        return TipoTaxaEnum.SCORE_BAIXO