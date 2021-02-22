import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


class Database:
    def __init__(self) -> None:
        db_url = os.getenv('DB_URL')
        db_client = AsyncIOMotorClient(db_url)
        db = db_client[os.getenv('DB_NAME')]
        self.collections = {
            'fees': db.get_collection('fees'),
            'clients': db.get_collection('clients')
        }


    def get_collection(self, name: str):
        if name not in self.collections:
            raise Exception(f'Collection [ {name} ] not found')
        return self.collections[name]


    def get_collections(self):
        return self.collections
