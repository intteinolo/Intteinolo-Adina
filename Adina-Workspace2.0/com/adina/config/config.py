import json
import logging
import sys
from typing import Text
from com.adina.utilities.Utilities import Utilities
from com.adina.utilities.LoggerFactory import LoggerFactory
from pathlib import Path 

class Configuration():    

    def __init__(self) -> None:
        self.__utilities = Utilities()
        self.__rootPath = str(Path.home())
        self.__configuration = {
            "configFileName": self.__rootPath + "/Adina/Config/appConfig.json",
            "rootPath": self.__rootPath,
            "appPath": self.__rootPath + "/Adina",
            "configPath": self.__rootPath + "/Adina/Config",
            "logPath": self.__rootPath + "/Adina/Logs",
            "loggingNames": [
                {"logName": "Adina", "logLevel": "DEBUG"},
                {"logName": "MongoDB", "logLevel": "DEBUG"}
            ]            
        }
        self.__createStructure()

    def __createStructure(self) -> None:        
        self.__utilities.mkdirs(self.__configuration["appPath"])
        self.__utilities.mkdirs(self.__configuration["configPath"])
        self.__utilities.mkdirs(self.__configuration["logPath"])
        if self.__utilities.isFile(self.__configuration["configFileName"]):
            self.__configuration = self.__utilities.readJSonFromFile(self.__configuration["configFileName"])
        else:
            self.__utilities.writeJSonToFile(self.__configuration["configFileName"], self.__configuration)

    @property
    def appPath(self) -> Text:
        return self.__configuration["appPath"]
    
    @property
    def configPath(self) -> Text:
        return self.__configuration["configPath"]

    @property
    def logPath(self) -> Text:
        return self.__configuration["logPath"]

    @property
    def getLoggingNames(self) -> list:
        return self.__configuration["loggingNames"]
    
    def getLogger(self, logName) -> LoggerFactory:
        try:
            myLogger = None
            for element in self.getLoggingNames:
                logLevel = logging.DEBUG
                if element["logName"] == logName:                    
                    if element["logLevel"].upper() == "INFO":
                        logLevel = logging.INFO
                    elif element["logLevel"].upper() == "WARN":
                        logLevel = logging.WARN
                    elif element["logLevel"].upper() == "ERROR":
                        logLevel = logging.ERROR
                    elif element["logLevel"].upper() == "FATAL":
                        logLevel = logging.FATAL
                    myLogger =  LoggerFactory(logName, logLevel)
                    break
        except:
            myLogger = LoggerFactory("Adina", logging.DEBUG)    
            myLogger.logger.warn(sys.exc_info()[0])
        return myLogger

"""
def getLoggingConfiguration(self, logFileName) -> dict:
        try:
        except:


    def __writeConfigFile(self) -> bool:
        print("")
"""