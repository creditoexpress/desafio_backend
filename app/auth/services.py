import jwt

from datetime import datetime, timedelta

from app.infra.repositories.clients_repository import ClientsRepository
from .models import User
from .exceptions import ClientNotFound, Unauthorized


async def login(clients_repository: ClientsRepository, user: User):
    client = await clients_repository.find_by_cpf(cpf=user.cpf)
    if not client:
        raise ClientNotFound()

    if user.cellphone != client['cellphone']:
        raise Unauthorized()

    now = datetime.now()
    token_payload = {
        "iss": client['cpf'],
        "iat": now,
        "exp": now + timedelta(days=1)
    }
    return jwt.encode(token_payload, 'secret', algorithm='HS256')


async def authenticate(clients_repository: ClientsRepository, token: str):
    decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
    client = await clients_repository.find_by_cpf(cpf=decoded['iss'])
    if not client:
        raise ClientNotFound()
