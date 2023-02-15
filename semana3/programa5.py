"""
    programa1
    nombre = gustavo salome
    fecha = 31/01/23
    descripcion = formulas para sacar el area y perimetro de un 
    circulo
"""
base: None
altura: None
while True:
  try:
    base = float(input("Escriba la base del   triángulo: "))

    print("Debe escribir un número")

    altura = float(input("Escriba la altura  del triángulo :"))
    break
  except:
    print("Debe escribir un número.")
area = base * altura / 2

print("El área del triángulo es igual a:{}".format(area))

lado0 = float(input("lado0: "))
lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
perimetro = lado0 + lado1 + lado2
print("el perimetro del triangulo es:{}".format(perimetro))
