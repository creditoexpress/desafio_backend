from dotenv import load_dotenv

from .infra.api.v1.api import app
from .infra.database import Database
from .config.ioc import IOC
from .infra.repositories.clients_repository import ClientsRepository


@app.get('/health')
def get_health():
    return { 'status': 'UP' }
