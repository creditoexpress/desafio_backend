from pydantic import BaseModel


class User(BaseModel):
    cpf: str
    cellphone: str

    class Config:
        schema_extra = {
            "example": {
                "cpf": "41882728564",
                "cellphone": "6526332774",
            }
        }

