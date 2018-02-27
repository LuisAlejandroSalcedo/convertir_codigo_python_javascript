"""
Este es un sencillo script que nos permite convertir codigo Python a JavaScript y viceversa. 

El proceso se realiza gracias al modulo 'Jiphy' el cual puedes descargar ejecutando el siguiente comando: pip install jiphy

Es un script muy sencillo, y el cual necesita un poco de optimizacion (Eliminación de elementos irrelevantes e incervibles)
"""

import jiphy
import os

nameFileCode = "" # Nombre del archivo (py o js) que contiene el codigo que queremos convertir
nameFileConversion = "" # Nombre del archivo que contendra el codigo convertido

# Para extraer todo el texto del archivo con el codigo, declramos la funcion "getTextFile"
def getTextFile(nameFile):
    with open(nameFile, 'r') as File:
        code = File.read()
        File.close()
        return code

# Estas funciones crearan los archivos con su correspondiente extensión
def createCodeFilePy(nameNewFile, content):
    with open(nameNewFile,'w') as codeFile:
        codeFile.write(content)
        codeFile.close()
    print('Archivo "%s" creado con exito' % nameNewFile)

def createCodeFileJS(nameNewFile, content):
    with open(nameNewFile,'w') as codeFile:
        codeFile.write(content)
        codeFile.close()
    print('Archivo "%s" creado con exito' % nameNewFile)

# Esta función convierte coodigo python a javascript
def  convertToPy(nameFile):
    code = getTextFile(nameFile)
    codePy =jiphy.to.python(code)
    return codePy

# Esta función convierte codigo javascript a python
def convertToJS(nameFile):
    code = getTextFile(nameFile)
    codeJS = jiphy.to.javascript(code)
    return codeJS

def isExtension(string, ext):
    if string.endswith(ext):
        return string
    else:
        return string + ext

# La función "StartConvertion" inica todo el proceso de conversion
# Y se utilizan ciertas funciones adicionales para evitar malas entradas del usuario
def StartConvertion():
    print('\n')    
    print("********************* Conversión De Codigo - Python y JavaScript *********************")
    nameFileCode = input("Ingresa la ruta del archivo para convertir: ")
    if os.path.exists(nameFileCode):
        if nameFileCode.endswith('.py'):
            nameFileConversion = input("Ingrese la ruta y el nombre del nuevo archivo en donde se guardara la conversión: ")
            nameFile = isExtension(nameFileConversion, '.js')
            conJS = convertToJS(nameFileCode)
            createCodeFileJS(nameFile, conJS)
        elif nameFileCode.endswith('.js'):
            nameFileConversion = input("Ingrese la ruta y el nombre del nuevo archivo en donde se guardara la conversión: ")
            nameFile = isExtension(nameFileConversion, '.py')
            conPy = convertToPy(nameFileCode)
            createCodeFilePy(nameFile, conPy)
        else:
            print("Debe introducir la ruta de un archivo 'py' o 'js'")
            StartConvertion()
    else:
        print('La ruta "%s" no ha sido encontrada' % nameFileCode)
        StartConvertion()    

StartConvertion()






