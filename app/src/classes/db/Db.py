import sys, os
import pymongo
from pymongo import MongoClient

BASE_PATH = os.path.abspath(__file__+ '/../../../../')
sys.path.append(BASE_PATH)

from src.consts.consts import *

class DbLib:

	def __init__(self):
		pass
	
	def connect(self, db="desafio"):
		client = 
			MongoClient(
				host       = DBHOST,
				port       = 27017, 
				username   = DBUSERNAME, 
				password   = DBUSERPASS,
				authSource = DBUSERAUTH
			)
		db = client[db]
		return db
