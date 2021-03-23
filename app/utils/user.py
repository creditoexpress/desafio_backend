from models import User

def return_user_json( func ):
    def a( *args, **kwargs ):
        return User.to_json( func( *args, **kwargs ) )
    return a