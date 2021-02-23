import json
import io


def parse_seed_file():
    fees_seeds = json.loads(io.open('./data/fees.json', encoding='utf-8').read())
    parsed_seeds = []
    for fee in fees_seeds:
        fee_values = fee['taxas']
        fees_portions = []
        for portions, value in fee_values.items():
            fees_portions.append({
                'portions': int(portions),
                'value': value
            })
        parsed_seeds.append({
            'fee_type': fee['tipo'],
            'fee_values': fees_portions
        })
    return parsed_seeds 


async def seed(fees_collection):
    fees = parse_seed_file()
    await fees_collection.insert_many(fees)
