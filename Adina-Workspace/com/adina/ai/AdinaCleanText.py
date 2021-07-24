from com.adina.utilities.JSON import JSonObject
import string


"""
This class contains the text cleaning processes to prepare the data for machine learning.
The routines that make it up are:

"""


class CleanOptions:

    def __init__(self):
        #self.dictionary = self.fromJson(anyJsonString)
        #print("Nombre documento = ",id(self))
        print("'Class CleanOptions iniciada'")
        return None
    
    # Genera una lista con el contenido de las páginas de un registro
    def getTextfromDocument(self, jsonObject):

        list_paginas = []

        for i in range (len(jsonObject.pages)):

            list_paginas.append(jsonObject.pages[i]['pageContent'])

        return list_paginas
    
    # Regresa el string a minúsculas
    def toMinusculas(self, tex_aux):

        return tex_aux.lower()

    # Manejo de ortografía, se estandarizan palabras sin acentos
    def limpiezaAcentos(self, tex_aux):

        tex_aux = tex_aux.replace("á", "a")
        tex_aux = tex_aux.replace("é", "e")
        tex_aux = tex_aux.replace("í", "i")
        tex_aux = tex_aux.replace("ó", "o")
        tex_aux = tex_aux.replace("ú", "u")

        return tex_aux

    # Manejo de signos de puntuación y carácteres especiales
    def limpiezaCaracteresEspeciales(self, tex_aux):

        tex_aux = tex_minus.replace(".", " ")
        tex_aux = tex_aux.replace(",", " ")

        table = str.maketrans('', '', string.punctuation)
        tex_aux = tex_aux.translate(table)

        tex_aux = tex_aux.replace("“", "")
        tex_aux = tex_aux.replace("”", "")

        return tex_aux




