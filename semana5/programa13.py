"""
    programa13
    Nombre: Gustavo Iván Salome Jimenez
    Fecha: 14/02/2023
    Descripcion: Herencia
"""

class Persona:
    def __init__(self): # definicion creada porcualquier usuario
          print("Persona") # mostrar texto en pantalla

class Alumno(Persona):
      def __init__(self): # definicion creada porcualquier usuario
            super().__init__() # permite invocar y conservar un método o atributo de una clase
            print("Alumno") # mostrar texto en pantalla

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.nombre ="Dejah Thoris"
print(objeto_persona.nombre)

objeto_alumno.nombre ="John Carter"
print(objeto_persona.nombre) # mostrar texto en pantalla

objeto_alumno.email ="john@utectulancingo.edu.mx"
print(objeto_alumno.email) # mostrar texto en pantalla

print(dir(objeto_persona)) # mostrar texto en pantalla
print(dir(objeto_alumno)) # mostrar texto en pantalla