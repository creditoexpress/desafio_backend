import json, logging

from service import user as user_service

def insert_users( users ):
    response = None
    try:
        response = user_service.insert_users( users )

    except Exception as e:
        logging.error( e )
        return "Falha ao inserir usuarios", 500
    
    else:
        return json.dumps( response )

def get_user_id_by_cpf_and_cellphone( user ):
    try:
        user = user_service.find_user_by_cpf_and_cellphone( user['cpf'], user['celular'] )
        if user:
            return str( user.id )
        else:
            logging.info( "Usuario visitante" )
            return 0
        
    except Exception as e:
        logging.error( e )
        return "Falha ao buscar usuario", 500
    