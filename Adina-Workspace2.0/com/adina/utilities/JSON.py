from com.adina.utilities.GSON import GSonObject
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
        self.dictionary = self.fromJson(anyJsonString)
            
    def toJson(self):
        anyString = None
        try:
            anyString = self.toJson(self, self.dictionary)
        except:
            anyString = None  
        return anyString    