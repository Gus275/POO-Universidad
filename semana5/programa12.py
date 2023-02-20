""" 
 nombre: Gustavo Iván Salomé Jiménez  
 fecha:14/02/2023 
 descripcion: se conocera la funcion self. 
 """ 
 class Persona:# crea la persona 
   def __init__(self):# se crea el tipo de letra 
          __nombre=None 
                  print("Persona")# se imprime la variable persona 
  
 class Alumno(Persona):# se crea la clase alumno persona 
   def __init__(self):# se crea el tipo de letra 
                 super().__init__() 
                 print("Alumno")# imprime la variable alumno 
  
 objeto_persona=Persona()# se crea el objeto persona 
 objeto_alumno=Alumno()# se cera el objeto alumno 
  
 objeto_persona.nombre="Dejah Thoris"# se crea el objeto persona y escrible el nombre de la variable 
 print(objeto_persona.nombre)# se imprime el objeto persona.nombre