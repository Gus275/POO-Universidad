"""
    programa16
    Nombre: Gustavo Iván Salome Jimenez
    Fecha: 15/02/2023
    Descripcion: Clase alumno
"""
from Persona import Persona
class Alumno(Persona): # Crear la clase Profesor del archivo persona .py
    def __init__(self) -> None: # construccion de la claase Profesor
        super().__init__() # Llama al constructor de la clase persona
        print("Alumno")  # imprime el texto profesor

objeto_alumno = Alumno() # Crea un objeto de la clase Profesor