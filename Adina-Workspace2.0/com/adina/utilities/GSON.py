import json

"""
This class has two methods to work with JSON notation.
fromJson - converts any valid Json string to a Dictionary object, it returns None if an error ocurrs.
toJson - receives a dictionary object and converts it to a JSon valid string.
"""

class GSonObject:   

    def fromJson(self, anyJsonString):
        dictionary = None
        try:
            dictionary = json.loads(anyJsonString)
        except:
            dictionary = None
        return dictionary

    def toJson(self, anyDictionaryObj):
        anyString = None
        try:
            anyString = json.dumps(anyDictionaryObj)
        except:
            anyString = None  
        return anyString