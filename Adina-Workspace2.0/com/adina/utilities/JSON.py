from typing import Text
from com.adina.utilities.GSON import GSonObject
import json

"""
JSonObject is a Subclass of GSonObject, it adds a dictionary object and expose all GSonObject methods. Thi is gone to be used to act as the masterclass of all the
mongoDB documents
"""

class JSonObject(GSonObject):   
    
    def __init__(self, anyJsonString):
        self.__dictionary = {
            "isEmpty": True
        }
        self.__dictionary = self.fromJson(anyJsonString)
            
    def toJson(self) -> Text:
        anyString = None
        try:
            anyString = self.toJson(self, self.__dictionary)
        except:
            anyString = None  
        return anyString    

    @property
    def dictionary(self) -> dict:
        return self.__dictionary