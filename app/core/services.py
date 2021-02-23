from ..infra.repositories.clients_repository import ClientsRepository
from ..infra.repositories.fees_repository import FeesRepository

from .exceptions import FeeNotFound

MEDIUM_SCORE = 500


def check_fee_type(score: int, negative: bool) -> str:
    if negative:
        return 'NEGATIVADO'

    return 'SCORE_ALTO' if score > MEDIUM_SCORE else 'SCORE_BAIXO'


def get_score_and_negative(client: dict):
    if not client:
        return 0, False

    return client['score'], client['negative']


async def get_fee(
    cpf: str, 
    portions: int,
    fees_repository: FeesRepository,
    clients_repository: ClientsRepository
):
    client = await clients_repository.find_by_cpf(cpf=cpf)

    score, negative = get_score_and_negative(client=client)
    fee_type = check_fee_type(score=score, negative=negative)

    fee = await fees_repository.find_by_type(fee_type=fee_type)
    fee_value = next((fee_value for fee_value in fee['fee_values']
                    if fee_value['portions'] == portions), None)

    if not fee_value:
        raise FeeNotFound()

    return fee_value['value']
