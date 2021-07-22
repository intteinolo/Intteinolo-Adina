from io import open
from pathlib import *

# Regresa el path del directorio de trabajo, que por omisión se esté usando
def getPath():    
    return str(Path.cwd())

# Abre un archivo con el modo de apertura que reciba
def openFile(fileName, openMode):
    try:
        file = open(getPath() + "/" + fileName, openMode)
        return file
    except Exception:
        return None

# Escribe una cadena a una archivo, si el archivo existe agrega la cadena, si no existe lo crea primero
# A la cadena que recibe le agrega un salto de linea
def writelnToFile(fileName, anyString):
    newFileName = getPath() + "/" + fileName
    try:
        file = open(newFileName, "a+") # Abre el archivo
        file.write(anyString + "\n")
        file.close()
        return True
    except Exception:
        return False

# Escribe una cadena a una archivo, si el archivo existe agrega la cadena, si no existe lo crea primero
def writeToFile(fileName, anyString):
    newFileName = getPath() + "/" + fileName
    try:
        file = open(newFileName, "a+") # Abre el archivo
        file.write(anyString)
        file.close()
        return True
    except Exception:
        return False