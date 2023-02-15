"""
nombre: Gustavo Iván Salome Jimenez
Fecha :01/02/2023
Descripcion: comparar 2 numeros enteros e imprimir el aumento mayor
"""
numero1= int(input("escribe el primer numero :")) # validar el primer numero

numero2= int(input("escribe el segundo numero :")) # validar el segundo munero
if numero1>=numero2: # verifica cual de los dos numeros es mayor o iguales
   print("el numero1 es mayor :{}".format(numero1)) # se imprime el numer1 como mayor
elif numero2>=numero1:
    print("el numero2 es mayor :{}".format(numero2)) # se imprime el numero2 como mayor
