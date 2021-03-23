import jwt
import traceback

from time import time
from flask import request

from auth import AUTH_HEADER_NAME

SECRET_KEY = 'chave-secreta-do-usuario'
ALGORITHM = 'HS256'

def generate_user_token( func ):
    def a( *args, **kwargs ):
        user_id = func( *args, **kwargs )
        
        if type(user_id) == tuple:
            return user_id

        payload = {
            'uid': user_id,
            'exp': int(time()) + 3600
        }

        return "Bearer {}".format( jwt.encode( payload, SECRET_KEY, algorithm = ALGORITHM ).decode( 'utf-8' ) )

    return a

def validate_user_token_and_get_id( func ):
    def a( *args, **kwargs ):
        try:
            user_token = request.headers.get( AUTH_HEADER_NAME )
            user_token = user_token.split()[-1]
            user_id = jwt.decode( user_token, SECRET_KEY, algorithms = [ ALGORITHM ] )

            user_id = user_id[ 'uid' ]

            return func( user_id, *args, **kwargs )

        except Exception as e:
            traceback.print_exc()
            return "Authentication fail", 500
    return a

