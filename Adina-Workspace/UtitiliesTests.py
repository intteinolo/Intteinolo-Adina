from com_utilities_adina.JSON import JSonObject
from com_utilities_adina.MasterObject import MasterObject
from com_businessRules_adina.AdinaObjects import User, DocumentType
from itertools import permutations, combinations

persona = JSonObject('{"firstName": "Carlos", "middleName": "Eduardo", "lastName": "Rodriguez", "telefonos": [{"tipo": "movil", "numero": "4422866800"}, {"tipo": "movil", "numero": "5532424474"}]}')

print(type(persona.dictionary))
print(persona.dictionary["firstName"])
print(persona.dictionary["telefonos"])
print(type(persona.dictionary["telefonos"]))

class Persona(MasterObject):

    def __init__(self) -> None:
        jsonString = '{"firstName": "", "middleName": "", "lastName": "", "telefonos": [{"tipo": "movil", "numero": ""}, {"tipo": "casa", "numero": ""}]}'
        super().__init__("Persona", jsonString)
    

carlos = Persona()

print(type(carlos))
print(carlos.firstName)
carlos.middleName = "Eduardo"
carlos.firstName = "Juan"
print(type(carlos.telefonos))
print(carlos.telefonos)
print(carlos.toJson())
carlos.email = "intteinolo@gmail.com"
print(carlos.toJson())


"""
rosa = User("correo@dominio.com")
rosa.firstName = "Rosa"
rosa.middleName = "Martinez"
print(rosa.toJson())
print(type(rosa.connected))
print(rosa.isConnected())
rosa.setConnected(True)
print(rosa.toJson())

rosaSt = rosa.toJson()

pdfDocument = DocumentType()

print(pdfDocument.EXCEL)

juan = User("id")
juan.fromJson(rosaSt)
juan.firstName = "Juan"
print(juan.toJson())

# Sin repeticiones n!
elements = ["A","B", "C", "D", "E", "F"]
per = [element for element in permutations(elements, 4)]
#print(per)
print(f"permutations: {len(per)}\n\n")

# Combinaciones n en r    n!/(n-r)!r!
elements = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
comb = [element for element in combinations(elements,3)]
print(comb)
print(f"Combinations1: {len(comb)}")
"""