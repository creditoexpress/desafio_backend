from typing import List
from pydantic import BaseModel, Field
from uuid import uuid4


class Client(BaseModel):
    id: str = Field(default_factory=uuid4, alias='_id')
    name: str
    cpf: str
    cellphone: str
    score: int = Field(..., gt=0, lt=1000)
    negative: bool

    class Config:
        schema_extra = {
            "example": {
                "name": "Roberto Filipe Figueiredo",
                "cpf": "41882728564",
                "cellphone": "6526332774",
                "score": 300,
                "negative": False,
            }
        }


class FeeByPortions(BaseModel):
    portions: int
    value: float

    class Config:
        schema_extra = {
            "example": {
                "portions": 6,
                "value": 0.03
            }
        }


class Fee(BaseModel):
    fee_type: str
    fee_values: List[FeeByPortions]

    class Config:
        schema_extra = {
            "example": {
                "fee_type": "NEGATIVADO",
            }
        }


class Simulation(BaseModel):
    value: float
    portions: int

    class Config:
        schema_extra = {
            "example": {
                "value": 10000,
                "portions": 6
            }
        }
