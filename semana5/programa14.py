class Profesor(Persona): # crea la clase Profesor que hereda 
     def __init__(self)-> None: # contructor de la clase  
         super().__init__() # llama la constructor de la clase Persona 
         print("Profesor") # imprime el texto profesor 
  
 objeto_profesor = Profesor() # crea un objetico de la clase Profesor 