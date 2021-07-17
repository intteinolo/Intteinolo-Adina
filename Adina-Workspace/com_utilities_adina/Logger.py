import logging
import logging.config
from typing import Text

class Logger():

    def __init__(self, logName) -> None:
        self.__logName = logName
        self.__logger = logging.getLogger(logName)

    def logName(self) -> Text:
        return self.__logName

    