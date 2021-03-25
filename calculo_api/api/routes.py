from flask_restful import Api

from api.calculos import CalculoApi

def create_routes(api: Api):

    api.add_resource(CalculoApi, '/calculo')