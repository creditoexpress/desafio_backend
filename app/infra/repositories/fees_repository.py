from ..database import get_collections


class FeesRepository:
    def __init__(self) -> None:
        self.fees = get_collections()['fees']

    async def find_by_type(self, fee_type: str):
        return self.fees.find_one({ 'fee_type': fee_type })
