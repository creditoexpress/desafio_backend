from flask_restful import Api

from api.taxa import TaxasApi, TaxaApi

def create_routes(api: Api):

    api.add_resource(TaxaApi, '/taxa')
    api.add_resource(TaxasApi, '/taxas')