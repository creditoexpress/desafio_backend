import json
import io


def parse_seed_file():
    seeds = json.loads(io.open('./data/clients.json', encoding='utf-8').read())
    parsed_seeds = []
    for client in seeds:
        parsed_seeds.append({
            "name": client['nome'],
            "cpf":  client['cpf'],
            "cellphone": client['celular'],
            "score": client['score'],
            "negative": client['negativado']
        })
    return parsed_seeds 


async def seed(clients_collection):
    clients = parse_seed_file()
    await clients_collection.insert_many(clients)
