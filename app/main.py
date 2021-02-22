import os

from dotenv import load_dotenv
from typing import Optional
from fastapi import FastAPI
# from .infra.database import get_collections
# from .config.ioc import IOC

load_dotenv()

app = FastAPI()


# @app.on_event('startup')
# async def set_db_client():
#     ioc = IOC()
#     collections = get_collections()
#     # for name, collection in collections.items():
#         # ioc.add(name, collection)
#     app.ctx = ioc


@app.get('/health')
def get_health():
    return { 'status': 'UP' }
