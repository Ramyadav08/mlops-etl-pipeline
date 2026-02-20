import os 
import json
import sys
from dotenv import load_dotenv
load_dotenv()
import certifi
import pandas as pd    
import numpy as np
from networksecurity.logging.logger import logging
from networksecurity.exception.exceptions import NetworkSecurityException
from pymongo.mongo_client import MongoClient
import pymongo

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
ca=certifi.where()


class NetworkDataExract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
    def csv_to_json(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(inplace=True,drop=True)
            json_data=df.to_json(orient='records')
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
    def insert_data_to_database(self,json_data,collection,database):
        try:
            self.database=database
            self.collection=collection
            self.json_data=json_data
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(json.loads(self.json_data))
            return len(json.loads(self.json_data))
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
if __name__=="__main__":
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="ETL"
    COLLECTION="NetworkData"
    networkobj=NetworkDataExract()
    record=networkobj.csv_to_json(file_path=FILE_PATH)
    print(record)
    no_of_records=networkobj.insert_data_to_database(json_data=record,collection=COLLECTION,database=DATABASE)
    print(f"{no_of_records} records inserted to database successfully")
    
    