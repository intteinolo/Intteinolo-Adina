import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])

print(x)

plt.plot(x, x)
plt.show()


# cargando text
pathname = '/home/intteinolo/Rosa Trabajo/Adina-Workspace/com_ai_adina/'
filename = 'example.txt'
file = open(pathname + filename, encoding="utf8")
text = file.read()
file.close()


# dividimos palabras por un espacio en blanco
words = text.split()
# print(words[:500])

print(len(words))

# #1.Escapar caracteres HTML
# import HTMLParser
# html_parser = HTMLParser.HTMLParser()
# texto = html_parser.unescape(original_tweet)
 
# #2.Decodificar los datos
# texto = original_tweet.decode("utf8").encode(‘ascii’,’ignore’)
 
# #3.Eliminar palabras comunes
# # https://www.ranks.nl/stopwords/spanish
# PALABRAS_COMUNES = ["un", "una", "ir", "voy",....]
# palabras = texto.split()
# reformado = ['' if palabra in PALABRAS_COMUNES else palabra for palabra in palabras]
# texto = " ".join(reformado)
 
# #4.Eliminar puntuaciones
# # CUIDADO! elimina todo tipo de puntuacion, las comas, 
# # puntos, signos de admiracion y pregunta pueden ser
# # necesarios y no deberían ser eliminados
# import string
# texto = texto.translate(None, string.punctuation)
 