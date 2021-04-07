from mongoengine import connect, disconnect
from pymongo import MongoClient
from os import getenv

class Database:
    
    def __init__(self):
        username = getenv('DB_USER')
        password = getenv('DB_PASS')
        cloud_host = getenv('DB_HOST')

        self.host = 'mongodb+srv://{}:{}@{}'.format(username, password, cloud_host)
        self.db_alias = 'mongocloud'
        self.db = 'ce_database'
        
        client = MongoClient(self.host)
        self.database = client['ce_database']
        
        
    def connect_db(self):
        connect(host=self.host, alias=self.db_alias, db=self.db)
        
    def disconnect_db(self):
        disconnect(alias=self.db_alias)