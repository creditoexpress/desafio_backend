import secrets

from dotenv import load_dotenv
from fastapi import FastAPI

from .database import Database
from ..config.ioc import IOC
from .repositories.fees_repository import FeesRepository
from .repositories.clients_repository import ClientsRepository


load_dotenv()

SECRET_SIZE = 64
JWT_SECRET = secrets.token_hex(SECRET_SIZE)


def create_app():
    app = FastAPI()
    db = Database()
    app.ctx = IOC()
    
    collections = db.get_collections()
    fees_repository = FeesRepository(collections['fees'])    
    clients_repository = ClientsRepository(collections['clients'])

    app.ctx.add('fees_repository', fees_repository)
    app.ctx.add('clients_repository', clients_repository)
    app.ctx.add('jwt_secret', JWT_SECRET)

    return app
