from enum import Enum
from com_utilities_adina.MasterObject import MasterObject

class DocumentType():

    def __init__(self) -> None:
        self.PDF = 1
        self.WORD = 2
        self.EXCEL = 3

class User(MasterObject):

    def __init__(self, id) -> None:
        anyJsonString = '{"firstName": "", "middleName": "", "lastName": "", "email": "", "mobileNumber": "", "connected": false, "userRoles": [{"administrator": false, "manager": false, "query": true}]}'
        super().__init__(id, anyJsonString)
    
    def isConnected(self) -> bool:
        return self.connected

    def setConnected(self, connected):
        self.connected = connected

class AdinaDocument(MasterObject):    

    def __init__(self, id) -> None:
        anyJsonString = '{"", ""}'
        super().__init__(id, anyJsonString)

    def __init__(self, id, anyJsonString) -> None:
        super().__init__(id, anyJsonString)    