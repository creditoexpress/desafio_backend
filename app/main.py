import os

from dotenv import load_dotenv
from typing import Optional
from fastapi import FastAPI
from .infra.database import Database
from .config.ioc import IOC
from .api.v1.api import router
from .infra.repositories.clients_repository import ClientsRepository

load_dotenv()

app = FastAPI()


@app.on_event('startup')
async def set_app_ctx():
    db = Database()
    ioc = IOC()

    collections = db.get_collections()
    # fees_repository = collections['fees']

    clients_repository = ClientsRepository(collections['clients'])
    ioc.add('clients_repository', clients_repository)

    app.ctx = ioc


@app.get('/health')
def get_health():
    return { 'status': 'UP' }


app.include_router(router)
