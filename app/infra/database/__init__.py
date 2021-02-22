import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


def get_connection():
    db_url = os.getenv('DB_URL')
    return AsyncIOMotorClient(db_url)


def get_collections():
    db_client = get_connection()
    db = db_client[os.getenv('DB_NAME')]
    return {
        'fees': db.get_collection('fees'),
        'clients': db.get_collection('clients')
    }
