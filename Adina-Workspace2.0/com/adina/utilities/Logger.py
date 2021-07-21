import os
import logging
import logging.config
from typing import Text
from datetime import datetime
from pathlib import Path 

class Logger():

    def __init__(self, logName, logLevel) -> None:
        self.__logName = logName
        try:
            os.makedirs(str(Path.home()) + "/Adina/Logs")
        except:
            None    
        default_log_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s", "%d/%m/%Y %H:%M:%S")
        file_handler = logging.handlers.RotatingFileHandler(str(Path.home()) + "/Adina/Logs/" + logName + "-" + datetime.now().strftime("%Y%m%d") + ".log", maxBytes=10485760,backupCount=300, encoding='utf-8')
        file_handler.setLevel(logLevel)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(default_log_formatter)
        console_handler.setFormatter(default_log_formatter)
        self.__logger = logging.getLogger(logName)
        self.__logger.setLevel(logLevel)
        if (self.__logger.hasHandlers()):
            self.__logger.handlers.clear()
        self.__logger.addHandler(file_handler)
        self.__logger.addHandler(console_handler)

    @property
    def logName(self) -> Text:
        return self.__logName

    @property
    def logger(self) -> logging.LoggerAdapter:
        return self.__logger