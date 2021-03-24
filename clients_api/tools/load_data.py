from models.clients import Client
import pymongo
import json


def seeders(root_dir):

    f = open(root_dir + "/resources/clients.json")

    data = json.load(f)
    clients_instances = [Client(**infos) for infos in data]

    clients = Client.objects()

    if not(clients):
        Client.objects.insert(clients_instances, load_bulk=False)

    return True

