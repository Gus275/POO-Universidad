"""
    programa11
    Nombre: Gustavo Iván Salome Jimenez
    Fecha: 13/02/2023
    Descripcion: Programa que utiliza clase persona e imprime elnombre y correo 
"""

class Persona:
    __nombre = None # denota falta de valor
    __email = None # denota falta de valor
    def __init__(self): # definicion creada porcualquier usuario 
        print("Persona")
    def setNombre(self,nombre):  # definicion creada porcualquier usuario
        self.__nombre = nombre
    def getNombre(self):  # definicion creada porcualquier usuario
        return self.__nombre
    def setEmail(self,email):  # definicion creada porcualquier usuario
        self.__email = email
    def getEmail(self):  # definicion creada porcualquier usuario
        return self.__email   #  final de la función y continúa la ejecución del programa tras la llamada a la función

dejah = Persona()

dejah.setNombre("Dejah") 
print (dejah.getNombre())

dejah.setEmail("correo@mascorreo.correo") 
print (dejah.getEmail())