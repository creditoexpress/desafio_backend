class SimulationRequest:
    def __init__(self, fee, value, portions):
        self.fee: float = fee 
        self.value: float = value 
        self.portions: int = portions

    def to_dict(self):
        return {
            'fee': self.fee,
            'value': self.value,
            'portions': self.portions
        }
