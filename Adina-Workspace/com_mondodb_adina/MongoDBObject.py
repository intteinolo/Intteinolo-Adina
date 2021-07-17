from typing import Collection, List, Text
import pymongo
import certifi
from pprint import pprint
from pymongo.database import Database

from pymongo.mongo_client import MongoClient

"""
"mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net/Adina2021"
"mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net/Adina2021?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
print(type(client))
print(client.list_database_names())
db=client.Adina2021
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
"""

class MongoDBObject():

    def __init__(self, CONNECTION_STRING) -> None:
        self.__CONNECTION_STRING = CONNECTION_STRING
        self.__mongoClient = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
        self.__connectedDataBase = None
        self.__errorFlag = False
        self.__errorDescription = ""

    def __resetError(self) -> None:
        self.__errorFlag = False
        self.__errorDescription = ""

    def __raiseError(self, errorDescription) -> None:
        self.__errorFlag = True
        self.__errorDescription = errorDescription

    def showLastError(self) -> Text:
        return self.__errorDescription

    def errorFlag(self) -> bool:
        return self.__errorFlag

    def mongoClient(self) -> MongoClient:
        return self.__mongoClient

    def connectToDatabase(self, dataBaseName) -> bool:
        try:
            self.__connectedDataBase = self.__mongoClient.get_database(dataBaseName)
            self.__resetError()
            return True
        except:
            self.__raiseError(f"An error ocurrs connecting to {dataBaseName} data base.")
            self.__connectedDataBase = None
            return False

    def connectedDataBase(self) -> Database:
        return self.__connectedDataBase

    def createCollection(self, collectionName) -> Collection:
        try:
            collectionNames = self.__connectedDataBase.list_collection_names()
            print(collectionNames)
        except:
            return None
    
    def showCollections(self) -> List:
        try:
            return self.__connectedDataBase.list_collection_names()
        except:
            return None


mongoDBObject = MongoDBObject("mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net")
print(type(mongoDBObject))
print(mongoDBObject.mongoClient().list_database_names())
print(mongoDBObject.connectToDatabase("Adina2021"))
print(mongoDBObject.connectedDataBase().name)
print(mongoDBObject.showCollections())
