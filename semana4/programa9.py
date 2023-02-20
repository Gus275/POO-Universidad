"""
    programa1
    nombre = gustavo salome
    fecha = 23/01/23
    descripcion = en este codigo se van a conocer los comentarios, 
    multilinea y concateneacion
"""

def mayor(numero1,numero2): # se define el valor de las variables numero1 y numero2

    if numero1>numero2:# se hace la operacion para saber si numero1 es mayor que numero2
      print("el numero1 es mayor :{}".format(numero1)) # se imprime el resultado de la variable numero1
    elif numero2>numero1: # se hace la operacion para saber si numero2 es mayor que numero1
      print("el numero2 es mayor :{}".format(numero2)) # se imprime el resultado de la variable numero2

    else:
     print("iguales") # imprime si las variables son iguales

mayor(3,2) # se imprime que numero es mayor
mayor(2,3) #se imprime que variable es menor
mayor(3,3)#se imprime los valores que son iguales