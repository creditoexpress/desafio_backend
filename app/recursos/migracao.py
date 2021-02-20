import json
import urllib
import logging
from flask import Response, request
from flask_restful import Resource
from mongoengine.errors import DoesNotExist

from db.modelos.taxa import Taxa
from db.modelos.cliente import Cliente

class MigracaoApi(Resource):
    def get(self):

        req = urllib.request.Request('https://raw.githubusercontent.com/creditoexpress/desafio_backend/master/taxas.json')
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)

        for v in values:
            v["taxas"] = json.dumps(v["taxas"])
            try:
                Taxa.objects.get(tipo=v["tipo"]).update(**v)
            except DoesNotExist:
                Taxa(**v).save()
        
        taxas = Taxa.objects.to_json();
        print(' --- TAXAS MIGRADAS ---')

        req = urllib.request.Request('https://raw.githubusercontent.com/creditoexpress/desafio_backend/master/clientes.json')
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)

        print('t clientes', len(values))
        
        for v in values:

            v["nome"] = str(v["nome"])
            v["cpf"] = str(v["cpf"])
            v["celular"] = str(v["celular"])
            v["score"] = int(v["score"])
            v["negativado"] = bool(v["negativado"])

            try:
                Cliente.objects.get(cpf=v["cpf"]).update(**v)
            except DoesNotExist:
                Cliente(**v).save()

        clientes = Cliente.objects.to_json();
        print(' --- CLIENTES MIGRADOS ---')
        
        return Response(json.dumps({'taxas': taxas, 'clientes': clientes}), mimetype="application/json", status=200)