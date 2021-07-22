from com.adina.utilities.LoggerFactory import LoggerFactory
import sys
import pymongo
import certifi
from pprint import pprint
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from com.adina.config.config import Configuration
from typing import Collection, List, Text

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

    def __init__(self, databaseConnectionName) -> None:
        self.__adinaConfiguration = Configuration()
        self.__mongoDBlogger = self.__adinaConfiguration.getLogger("MongoDB")
        self.__databaseConnectionName = databaseConnectionName
        self.__databaseConnection = self.__adinaConfiguration.getDataBaseConnection(self.__databaseConnectionName)
        self.__createMongoClient()

    def __createMongoClient(self) -> None:
        if self.__databaseConnection != None:
            self.__URI_CONNECTION_STRING = self.__databaseConnection["uri"]["srv"] + self.__databaseConnection["uri"]["user"] + ":" + self.__databaseConnection["uri"]["password"] + self.__databaseConnection["uri"]["cluster"] + self.__databaseConnection["uri"]["dataBase"]
            self.__mongoClient = pymongo.MongoClient(self.__URI_CONNECTION_STRING, tlsCAFile=certifi.where())
            self.__mongloClientCreated = True
            self.__connectedDataBase = None
            self.__errorFlag = False
            self.__errorDescription = ""
        else:
            self.__errorFlag = True
            self.__errorDescription = "Data base connection " + self.__databaseConnectionName + " not found in configure file, please verify."
            self.__URI_CONNECTION_STRING = ""
            self.__mongloClientCreated = False
            self.__mongoDBlogger.warn(self.__errorDescription)    

    @property
    def mongoDBlogger(self) -> LoggerFactory:
        return self.__mongoDBlogger

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
            if self.__mongloClientCreated:
                self.__connectedDataBase = self.__mongoClient.get_database(dataBaseName)
                self.__resetError()
                self.__mongoDBlogger.debug(f"Connected to {dataBaseName} database.")
                return True
            else:
                self.__mongoDBlogger.error(f"Mongo client not created for {dataBaseName}.")
                self.__raiseError(f"Mongo client not created for {dataBaseName}.")
                return False
        except:            
            self.__mongoDBlogger.error(f"An error ocurrs connecting to {dataBaseName} data base." + " --> " + sys.exc_info()[0])
            self.__raiseError(f"An error ocurrs connecting to {dataBaseName} data base." + " --> " + sys.exc_info()[0])
            self.__connectedDataBase = None
            return False

    def connectedDataBase(self) -> Database:
        return self.__connectedDataBase

    def createCollection(self, collectionName) -> Collection:
        try:
            collectionNames = self.__connectedDataBase.list_collection_names()
        except:
            self.__mongoDBlogger.error(f"An error ocurrs (createCollection)." + " --> " + sys.exc_info()[0])
            self.__raiseError(f"An error ocurrs (createCollection)." + " --> " + sys.exc_info()[0])
            return None
    
    def showCollections(self) -> List:
        try:
            return self.__connectedDataBase.list_collection_names()
        except:
            self.__mongoDBlogger.error(f"An error ocurrs (showCollections)." + " --> " + sys.exc_info()[0])
            self.__raiseError(f"An error ocurrs (showCollections)." + " --> " + sys.exc_info()[0])
            return None

    def collectionExists(self, collectionName) -> bool:
        try:
            collList = self.__connectedDataBase.list_collection_names()
            if collectionName in collList:
                return True
            else:    
                return False
        except:
            self.__mongoDBlogger.error(f"An error ocurrs (showCollections)." + " --> " + sys.exc_info()[0])
            self.__raiseError(f"An error ocurrs (showCollections)." + " --> " + sys.exc_info()[0])
            return False
    
    