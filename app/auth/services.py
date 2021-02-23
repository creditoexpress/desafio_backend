import jwt

from datetime import datetime, timedelta

from app.infra.repositories.clients_repository import ClientsRepository
from .models import User
from .exceptions import Unauthorized


async def login(clients_repository: ClientsRepository, user: User, jwt_secret: str):
    client = await clients_repository.find_by_cpf(cpf=user.cpf)

    if client and user.cellphone != client['cellphone']:
        raise Unauthorized()

    now = datetime.now()
    token_payload = {
        "iat": now,
        "iss": user.cpf,
        "exp": now + timedelta(days=1)
    }
    return jwt.encode(token_payload, jwt_secret, algorithm='HS256')


async def authenticate(token: str, jwt_secret: str):
    decoded = jwt.decode(token, jwt_secret, algorithms=['HS256'])
    cpf = decoded['iss']
    return cpf
