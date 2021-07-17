import json
from typing import Any

class MasterObject():

    def __init__(self, id, anyJsonString) -> None:
        self.fromJson(anyJsonString)
        self.id = id

    def fromJson(self, anyJsonString): 
        try:
            self.__dict__ = json.loads(anyJsonString)
        except:
            self.__dict__ = None
        return self.__dict__

    def toJson(self):
        anyString = None
        try:
            #anyString = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            anyString = json.dumps(self.__dict__)
        except:
            anyString = None  
        return anyString