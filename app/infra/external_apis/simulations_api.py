import json

from http3 import AsyncClient

from ...core.values import SimulationRequest


URL = 'https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend'
HEADERS = { 'Content-Type': 'application/json' }


async def get_simulation(simulation_request: SimulationRequest):
    try:
        client = AsyncClient()
        payload = simulation_request.to_dict()
        data = {
            "valor": payload['value'],
            "taxaJuros": payload['fee'],
            "numeroParcelas": payload['portions']
        }
        response = await client.post(url=URL, data=json.dumps(data), headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as ex:
        print(ex)
        return None
