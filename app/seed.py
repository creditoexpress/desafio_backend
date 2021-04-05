from json import loads
import sys

from args import treat_args
from app.models.cliente import Cliente
from app.models.taxa import Taxa
from app.services.database import Database


class Seed:


    @staticmethod
    def seed(argv):
        
        dir_clientes, dir_taxas = treat_args(argv)

        if dir_clientes and dir_taxas:
            Seed.seed_clientes(dir_clientes)
            Seed.seed_taxas(dir_taxas)
        elif dir_clientes:
            Seed.seed_clientes(dir_clientes)
        elif dir_taxas:
            Seed.seed_taxas(dir_taxas)


    @staticmethod
    def seed_clientes(dir_clientes):
        
        with open(dir_clientes, 'r') as arquivo_clientes:
            clientes_json = loads(arquivo_clientes.read())

        clientes = []

        for cliente_json in clientes_json:
            cliente = Cliente(
                                nome=cliente_json['nome'],
                                cpf=cliente_json['cpf'],
                                celular=cliente_json['celular'],
                                score=cliente_json['score'],
                                negativado=cliente_json['negativado']
            )
            clientes.append(cliente)
        
        Database().insert_clientes(clientes)


    @staticmethod
    def seed_taxas(dir_taxas):
        
        with open(dir_taxas, 'r') as arquivo_taxas:
            taxas_json = loads(arquivo_taxas.read())

        taxas = []

        for taxa_json in taxas_json:
            taxa = Taxa(
                        tipo=taxa_json['tipo'],
                        taxas=taxa_json['taxas']
            )
            taxas.append(taxa)
        
        Database().insert_taxas(taxas)


if __name__ == "__main__":
    Seed.seed(sys.argv[1:])