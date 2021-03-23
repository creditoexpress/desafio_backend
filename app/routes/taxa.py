from flask import Blueprint, request

import json
from controller import taxa as taxa_controller

taxa_routes = Blueprint( 'taxa', __name__, url_prefix = '/taxa' )

@taxa_routes.route( '/insert', methods = ['POST'] )
def insert_taxas():
    return taxa_controller.insert_taxas( request.get_json() )

@taxa_routes.route( '/insert-file', methods = ['POST'] )
def insert_taxas_by_file():
    file = json.load( request.files[ 'file' ] )
    return taxa_controller.insert_taxas( file )