from com.adina.utilities.JSON import JSonObject
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


"""
This class contains the text cleaning processes to prepare the data for machine learning.
The routines that make it up are:

"""


class CleanOptions:

    def __init__(self):
        
        self.__configuration = {"configCleanFileName": ""}
        print("'Class CleanOptions iniciada'")
        return None
    
    # # Genera una lista con el contenido de las páginas de un registro
    def getTextfromDocument(self, jsonObject):

        list_paginas = []

        for i in range (len(jsonObject.pages)):

            list_paginas.append(jsonObject.pages[i]['pageContent'])

        return list_paginas
    
    # # Regresa el string a minúsculas
    def toMinusculas(self, tex_aux):

        return tex_aux.lower()

    # # Manejo de ortografía, se estandarizan palabras sin acentos
    def limpiezaAcentos(self, tex_aux):

        tex_aux = tex_aux.replace("á", "a")
        tex_aux = tex_aux.replace("é", "e")
        tex_aux = tex_aux.replace("í", "i")
        tex_aux = tex_aux.replace("ó", "o")
        tex_aux = tex_aux.replace("ú", "u")

        return tex_aux

    # # Manejo de signos de puntuación y carácteres especiales
    def limpiezaCaracteresEspeciales(self, tex_aux):

        tex_aux = tex_aux.replace(".", " ")
        tex_aux = tex_aux.replace(",", " ")

        table = str.maketrans('', '', string.punctuation)
        tex_aux = tex_aux.translate(table)

        tex_aux = tex_aux.replace("“", "")
        tex_aux = tex_aux.replace("”", "")

        tex_aux = tex_aux.replace("  ", " ")
        
        return tex_aux

    # # Separación por palabras
    def separarPalabras(self, tex_aux):

        return word_tokenize(tex_aux)

    # # Diccionario de palabras a limpiar
    def diccionarioPalabrasVacias(self):

        # # Descarga de diccionario base

        stop_words = stopwords.words('spanish')

        bad_words = []
        for i in range(len(stop_words)):

            aux = self.limpiezaAcentos(stop_words[i])
            if aux not in bad_words:
                
                bad_words.append(aux)

        # # Preposiciones del español

        bad_words.append("bajo")
        bad_words.append("cabe")
        bad_words.append("hacia")
        bad_words.append("mediante")
        bad_words.append("segun")
        bad_words.append("so")
        bad_words.append("tras")
        bad_words.append("via")
        bad_words.append("pro")
        bad_words.append("excepto")
        bad_words.append("menos")
        bad_words.append("salvo")
        #bad_words.append("allende")
        bad_words.append("aquende")

        # # Preguntas

        bad_words.append("cuanto")
        bad_words.append("cuantos")
        bad_words.append("cuantas")
        bad_words.append("cuales")
        bad_words.append("cuanta")
        bad_words.append("adonde")

        # # Construcciones preposicionales

        bad_words.append("causa")
        #bad_words.append("fin")
        #bad_words.append("fuerza")
        bad_words.append("pesar")
        #bad_words.append("proposito")
        bad_words.append("acerca")
        bad_words.append("lado")
        bad_words.append("alrededor")
        bad_words.append("cerca")
        #bad_words.append("arreglo")
        #bad_words.append("objeto")
        #bad_words.append("relacion")
        bad_words.append("tal")
        bad_words.append("debajo")
        bad_words.append("delante")
        bad_words.append("dentro")
        bad_words.append("despues")
        bad_words.append("detras")
        bad_words.append("medio")
        bad_words.append("orden")
        bad_words.append("pos")
        bad_words.append("vez")
        #bad_words.append("virtud")
        bad_words.append("encima")
        bad_words.append("enfrente")
        bad_words.append("frente")
        bad_words.append("gracias")
        bad_words.append("junto")
        bad_words.append("lejos")
        bad_words.append("culpa")
        bad_words.append("respecto")
        bad_words.append("favor")
        bad_words.append("largo")
        bad_words.append("forme")
        bad_words.append("lugar")
        bad_words.append("incluso")
        #bad_words.append("condicion")

        return bad_words

    # # Eliminación de preposiciones del español
    def eliminacionPreposiciones(self, list_aux):

        # # Traer diccionario de palabras vacías
        bad_words = self.diccionarioPalabrasVacias()

        list_aux = [w for w in list_aux if not w in bad_words]

        return list_aux
    
    # # Obtener listado de parrafos de un string
    def getParrafos(self, str_aux):

        return sent_tokenize(str_aux)

    # # Reducción de palabras a la raíz
    def palabrasToRaiz(self, list_aux):

        list_new = []
        porter = SnowballStemmer('spanish') # PorterStemmer()
        for word in list_aux:

            if word.isalpha():

                list_new.append(porter.stem(word))
            else:

                list_new.append(word)
        
        return list_new
    
    # # # Identifica idioma, descarta palabras que no estén en español
    # def identificaIdioma(self, list_aux):

    #     import cld3
    
    #     list_new = []
    #     for word in list_aux:

    #         cld3.get_language("影響包含對氣候的變化以及自然資源的枯竭程度")
    #         if TextBlob(word).detect_language() == "es":

    #                 list_new.append(word)

    #     return list_new
    
    # # Diccionario de abreviaturas
    def diccionarioAbreviaturas(self):
        
        bad_words = []
        str_alphabet = string.ascii_lowercase
        list_alphabet = list(str_alphabet)

        for i in range(len(list_alphabet)):
            
            bad_words.append(list_alphabet[i])
        
        # # números aislados

        bad_words.append("0")
        bad_words.append("1")
        bad_words.append("2")
        bad_words.append("3")
        bad_words.append("4")
        bad_words.append("5")
        bad_words.append("6")
        bad_words.append("7")
        bad_words.append("8")
        bad_words.append("9")

        two_letters = []
        for i in range(len(bad_words)):

            for j in range(len(bad_words)):

                aux = ''.join([bad_words[i], bad_words[j]])
                two_letters.append(aux)

        three_letters = []
        for i in range(len(two_letters)):

            for j in range(len(bad_words)):

                aux = ''.join([two_letters[i], bad_words[j]])
                three_letters.append(aux)
        
        for i in range(len(two_letters)):

            bad_words.append(two_letters[i])
        
        for i in range(len(three_letters)):

            bad_words.append(three_letters[i])

        return bad_words

    # # Eliminación de abreviaturas español
    # # En este caso las abreviaturas se eliminan pero otra opción sería ampliar las palabras, ejemplo: sr:señor
    def eliminacionAbreviaturas(self, list_aux):

        # # Traer diccionario de abreviaturas
        bad_words = self.diccionarioAbreviaturas()
        
        list_aux = [w for w in list_aux if not w in bad_words]

        return list_aux

    # # Lemmatización de las palabras
    # # Es reducir las formas flexivas a una forma básica común. Utiliza bases de conocimiento léxico para obtener las formas básicas correctas de las palabras.
    def lematizacionPalabras(self, list_aux):

        lemmatizer = WordNetLemmatizer()
        for i in range(len(list_aux)):

            list_aux[i] = lemmatizer.lemmatize(list_aux[i])
        
        return list_aux

    # # La lista se depura a valores únicos
    def valoresUnicos(self, list_aux):

        list_new = []
        for i in range(len(list_aux)):
            
            if list_aux[i] not in list_new:
                
                list_new.append(list_aux[i])

        return list_new

    # # Rutina de limpieza completa
    def rutinaLimpieza(self, tex_aux):

        # # Conversión a minúsculas
        tex_aux = self.toMinusculas(tex_aux)

        # # Tratamiento ortográfico
        tex_aux = self.limpiezaAcentos(tex_aux)

        # # Manejo de signos de puntuación y carácteres especiales
        tex_aux = self.limpiezaCaracteresEspeciales(tex_aux)

        # # Separación por palabras
        list_aux = self.separarPalabras(tex_aux)

        # # Eliminación de preposiciones del español
        list_aux = self.eliminacionPreposiciones(list_aux)

        # # Eliminación de abreviaturas
        list_aux = self.eliminacionAbreviaturas(list_aux)

        # # Lemmatización de las palabras
        list_aux = self.lematizacionPalabras(list_aux)

        return list_aux






