from flask import Blueprint, request

from auth.user import validate_user_token_and_get_id
from controller import simulacao_emprestimo as simulacao_emprestimo_controller

simulacao_emprestimo_routes = Blueprint( 'simulacao_emprestimo', __name__, url_prefix = '/simulacao_emprestimo' )

@simulacao_emprestimo_routes.route( '/simular', methods = ['GET'] )
@validate_user_token_and_get_id
def simular_emprestimo( id_usuario ):
    return simulacao_emprestimo_controller.simular_emprestimo( id_usuario, request.get_json() )