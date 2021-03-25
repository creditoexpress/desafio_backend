from models.taxas import Taxa
import pymongo
import json


def seeders(root_dir):

    f = open(root_dir + "/resources/taxas.json")

    data = json.load(f)
    
    taxas_instances = [Taxa(**infos) for infos in data]

    taxas = Taxa.objects()

    if not(taxas):
        Taxa.objects.insert(taxas_instances, load_bulk=False)

    return True

