import os
import random
from com.adina.utilities.JSON import JSonObject
from com.adina.utilities.MasterObject import MasterObject
from com.adina.ai.AdinaCleanText import CleanOptions

# # El archivo a continuación se carga para propósitos de la prueba

pathname = str(os.path.dirname(__file__))
filename = '\example.txt'
completefilename = pathname + filename
file = open(pathname + filename, encoding="utf8")
text = file.read()
words = list(map(str, text.split()))
file.close()

# # Se definen las clases de los diccionarios para propósitos de la prueba

class auxDic:

    def __init__(self, dic_var, list_aux) -> None:

        self.dic_var = dic_var
        self.dic_var = dict(zip(self.dic_var, list_aux))

dic_parrafo = {"paragraphId": "1", "paragraphContent": ""}

var_str = ""
for i in range(10):

    var_str = var_str + random.choice(words) + ' '

parrafo1 = auxDic(dic_parrafo, [1, var_str])

var_str = ""
for i in range(10):

    var_str = var_str + random.choice(words) + ' '

parrafo2 = auxDic(dic_parrafo, [2, var_str])

# print(parrafo1.dic_var)
# print(parrafo2.dic_var)

dic_pagina = {"pageNumber": "1", "pageIndex": "", "pageContent": "", "paragraphs": ""}

list_parrafos = [parrafo1.dic_var, parrafo2.dic_var]
pagina1 = auxDic(dic_pagina, [1, 1, text, list_parrafos])
pagina2 = auxDic(dic_pagina, [2, 2, text, list_parrafos])

# print(pagina1.dic_var)
# print(pagina2.dic_var)

dic_origen = {"nombreEquipo": "", "usuarioEquipo": "", "ipEquipo": "", "pathDocumento": ""}
origen = auxDic(dic_origen, ['laptopRosa', 'Rosa', '123.123.123.123', completefilename])

#print(origen.dic_var)

list_paginas = [pagina1.dic_var, pagina2.dic_var]

class Registro(MasterObject):

    def __init__(self) -> None:
        jsonString = '{"idBinary": "1", "origen": "", "fileName": "", "documentType": "", "numberOfPages": "", "pages": ""}'
        super().__init__('Registro', jsonString)

registro = Registro()
registro.idBinary = 1
registro.origen = origen.dic_var
registro.fileName = filename
registro.documentType = "txt"
registro.numberOfPages = len(list_paginas)
registro.pages = list_paginas
# registro["origen"]["nombreEquipo"] = 'laptopRosa'
# print(registro["pages"])

# print(registro.toJson())

# # Pruebas de la bibliteca AdinaCleanText

json_ejemplo = registro.toJson()

# print(registro.pages[0])
# print(len(registro.pages[0]))

# print(registro.pages[0]['pageContent'])

print(type(registro.pages[0]['pageContent']))

# metodosLimpieza = CleanOptions()

# print(metodosLimpieza.getTextfromDocument())
























