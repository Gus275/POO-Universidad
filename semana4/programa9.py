"""
    programa1
    nombre = gustavo salome
    fecha = 23/01/23
    descripcion = en este codigo se van a conocer los comentarios, 
    multilinea y concateneacion
"""
def mayor(numero1,numero2):

    if numero1>numero2:
      print("el numero1 es mayor :{}".format(numero1))
    elif numero2>numero1:
      print("el numero2 es mayor :{}".format(numero2))

    else:
     print("iguales")

    mayor(3,2)
    mayor(2,3)
    mayor(3,3)