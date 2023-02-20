"""
    programa1
    nombre = gustavo salome
    fecha = 23/01/23
    descripcion = en este codigo se van a conocer los comentarios, 
    multilinea y concateneacion
"""
def mayor(numero1, numero2): # se define el valor de las variables numero1 y numero2
    if numero1>numero2: 
        print(numero1)
    elif numero2 > numero1:
        print(numero2) 
    else:
        print("none") #imprime si las variables son none
        
mayor (3,2)# 3 call
mayor (2,3) #3
mayor (3,3) #none