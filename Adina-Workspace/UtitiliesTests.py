from com_utilities_adina.JSON import JSonObject

persona = JSonObject('{"firstName": "Carlos", "middleName": "Eduardo", "lastName": "Rodriguez"}')

print(type(persona.dictionary))
print(persona.dictionary["firstName"])
