"""
    programa1
    nombre = gustavo salome
    fecha = 23/01/23
    descripcion = en este codigo se van a conocer los comentarios, 
    multilinea y concateneacion
"""
def  mayor(numero1:int,numero2:int): #se vide las variables  
        mayor=None# 
  if numero1 > numero2:# se hace la operación para saber que numero es mayor 
    mayor = (numero1) # se imprime el número 1 como mayor 
  elif numero2>numero1:# en caso que no sea real se pasa al siguiente operación para saber si el numero dos es mayor 
   mayor=(numero2)# se imprime el resultado del numero mayor en este caso es numero 2 
  else:  # en caso que no se cumpla la función de artiba se pasa hacia abajo  
    mayor= None# se denomida el mayor como none es decir que puede ser cualquier valor 
  return mayor# se vuelve hacer tdo lo anterior es decir de reinicia el proceso.