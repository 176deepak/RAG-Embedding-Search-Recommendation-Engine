import os
import sys
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.exception import CustomException


load_dotenv()
uri = os.getenv('CLUSTER_URI')

try:
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
except Exception as e:
    raise CustomException(e, sys)


def dataloader(db, collection, query={}, proj={}):
    db = client[db]
    collection = db[collection]
    
    try:
        records = collection.find(query, proj)
        return records
    except Exception as e:
        raise CustomException(e, sys)




    
    