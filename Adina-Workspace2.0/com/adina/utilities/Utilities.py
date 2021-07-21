import os
import sys
import json
import logging
import logging.config
from typing import Text
from pathlib import Path 
from datetime import datetime
from com.adina.utilities.LoggerFactory import LoggerFactory

class Utilities:

    def __init__(self) -> None:
        self.__rootPath = str(Path.home())
        print(self.__rootPath)    
        print(os.name)
        print(os.uname())
        self.mkdirs(self.__rootPath + "/Adina/Logs")
        self.__logger = LoggerFactory("Adina", logging.DEBUG)

    @property
    def rootPath(self) -> Text:
        return self.__rootPath

    def isDir(self, dirName) -> bool:
        return os.path.isdir(dirName)

    def isFile(self, fileName) -> bool:
        return os.path.isfile(fileName)

    def dirExists(self, dirName) -> bool:
        return os.path.exists(dirName)

    def mkdir(self, dirName) -> bool:
        try:
            os.makedir(dirName)
            return True
        except:
            logging.warn(sys.exc_info()[0])
            return False

    def mkdirs(self, dirName) -> bool:
        try:
            os.makedirs(dirName)
            return True
        except:
            logging.warn(sys.exc_info()[0])
            return False

    def writeToFile(self, fileName, anyString) -> bool:
        try:
            fileObject = open(fileName, "a")
            fileObject.write(anyString)
            fileObject.close()
            return True
        except:
            logging.error(sys.exc_info()[0])
            return False
    
    def renameFile(self, oldFileName, newFileName) -> bool:
        try:
            os.rename(oldFileName, newFileName)
            return True
        except:
            logging.error(sys.exc_info()[0])
            return False    

    def readJSonFromFile(self, fileName) -> dict:
        try:            
            with open(fileName, "r") as fileObject:
                jsonObject = json.load(fileObject)
            return jsonObject
        except:
            logging.error(sys.exc_info()[0])
            return None

    def writeJSonToFile(self, fileName, anyDictionaryObj) -> bool:
        try:
            with open(fileName, "w") as fileObject:
                json.dump(anyDictionaryObj, fileObject, ensure_ascii=True, indent=4, sort_keys=True)
            return True    
        except:
            logging.error(sys.exc_info()[0])
            return False
    
    def debug(self, anyString) ->  None:
        self.__logger.debug(anyString)

    def info(self, anyString) -> None:
        self.__logger.info(anyString)

    def warn(self, anyString) -> None:
        self.__logger.warn(anyString)

    def error(self, anyString) -> None:
        self.__logger.error(anyString)

    def fatal(self, anyString) -> None:
        self.__logger.fatal(anyString)