class FeesRepository:
    def __init__(self, collection) -> None:
        self.fees = collection

    def find_by_type(self, fee_type: str):
        return self.fees.find_one({ 'fee_type': fee_type })
