from dotenv import load_dotenv
from fastapi import FastAPI

from .database import Database
from ..config.ioc import IOC
from .repositories.clients_repository import ClientsRepository


load_dotenv()


def create_app():
    app = FastAPI()
    db = Database()
    app.ctx = IOC()
    
    collections = db.get_collections()
    # fees_repository = collections['fees']
    
    clients_repository = ClientsRepository(collections['clients'])
    app.ctx.add('clients_repository', clients_repository)

    return app
