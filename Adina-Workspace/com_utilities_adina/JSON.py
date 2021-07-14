from com_utilities_adina.GSON import GSonObject
import json

"""
JSonObject is a Subclass of GSonObject, it adds a dictionary object and expose all GSonObject methods. Thi is gone to be used to act as the masterclass of all the
mongoDB documents
"""

class JSonObject(GSonObject):   

    dictionary = {
        "isEmpty": True
    }
    
    def __init__(self, anyJsonString):
        self.dictionary = GSonObject.fromJson(anyJsonString)
    
    def fromJson(self, anyJsonString):
        self.dictionary = GSonObject.fromJson(self, anyJsonString)
        return self.dictionary

    def toJson(self, anyDictionaryObj):
        anyString = None
        try:
            anyString = GSonObject.toJson(self, anyDictionaryObj)
        except:
            anyString = None  
        return anyString

    def toJson(self):
        anyString = None
        try:
            anyString = GSonObject.toJson(self, self.dictionary)
        except:
            anyString = None  
        return anyString    