from persona import Persona # alumno importa de la clase persona 
 class Alumno(Persona):# crea la clase alumno que hereda la clase persona 
     def __init__(self) -> None: # construye de la clase alumno 
         super().__init__() # llama al constructor de la clase Alumno  
         print("Alumno") #  
  
 objeto_alumno = Alumno()# crea un objetico de la clase alumno. 
 