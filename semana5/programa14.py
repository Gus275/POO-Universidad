"""
    programa14
    Nombre: Gustavo Iván Salome Jimenez
    Fecha: 30/01/2023
    Descripcion: Clase persona
"""

class Persona:
    __nombre = None # denota falta de valor
    __edad = None # denota falta de valor
    def __init__(self) -> None: # definicion creada porcualquier usuario y denota falta de valor
        
        print("Persona")  # mostrar texto en pantalla
        
    def setNombre(self,nombre:str) -> None:  # definicion creada porcualquier usuario y denota falta de valor
 
        self.__nombre = nombre # modo de cálculo para hacer referencia al contenido del objeto
        
    def getNombre(self) -> str: # definicion creada porcualquier usuario
        return self.__nombre #  final de la función y continúa la ejecución del programa tras la llamada a la función