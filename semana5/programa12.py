"""
    programa12
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 13/02/2023
    Descripcion: Programa que utiliza clase persona e imprime el nombre, correo y carrera
"""

class Alumno:
    __nombre = None # denota falta de valor
    __matricula = None # denota falta de valor
    __carrera = None # denota falta de valor
    def __init__(self): # definicion creada porcualquier usuario
        print("Alumno") # mostrar texto en pantalla
    def setNombre(self,nombre): # definicion creada porcualquier usuario
        self.__nombre = nombre
    def getNombre(self): # definicion creada porcualquier usuario
        return self.__nombre  #  final de la función y continúa la ejecución del programa tras la llamada a la función
    def setMatricula(self,matricula): # definicion creada porcualquier usuario
        self.__matricula = matricula
    def getMatricula(self): # definicion creada porcualquier usuario
        return self.__matricula #  final de la función y continúa la ejecución del programa tras la llamada a la función
    def setCarrera(self,carrera): # definicion creada porcualquier usuario
        self.__carrera = carrera
    def getCarrera(self): # definicion creada porcualquier usuario
        return self.__carrera #  final de la función y continúa la ejecución del programa tras la llamada a la función

gustavo = Alumno()

gustavo.setNombre("gustavo") 
print (gustavo.getNombre())

gustavo.setMatricula("1722110099") 
print (gustavo.getMatricula())


gustavo.setCarrera("Desarrollo de Software") 
print (gustavo.getCarrera())