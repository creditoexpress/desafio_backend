import json

from models import User
from utils import return_user_json

@return_user_json
def insert_user( user ):
    user = User.from_json( json.dumps( user ) )
    user.save()
    return user

def find_user_by_cpf_and_cellphone( user_cpf, cellphone ):
    return User.objects( cpf = user_cpf, celular = cellphone ).first()

def find_user_by_id( user_id ):
    user = User.objects.get( id = user_id )
    return user