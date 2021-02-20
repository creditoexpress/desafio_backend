from .taxas import TaxaApi
from .migracao import MigracaoApi
from .clientes import ClienteApi
from .calculo import CalculoApi

def initialize_routes(api):

    api.add_resource(MigracaoApi, '/migracao')
    
    api.add_resource(ClienteApi, '/cliente/<cpf>/<celular>')
    
    api.add_resource(TaxaApi, '/taxa')

    api.add_resource(CalculoApi, '/calculo')