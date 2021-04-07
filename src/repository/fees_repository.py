from src.setup.database import Database

class FeesRepository:
    
    def __init__(self):
        self.collection = Database().database['taxas']
        
    def get_fee_by_type(self, fee_type):
        fee = self.collection.find_one({ 'tipo': fee_type })
        return fee['taxas']