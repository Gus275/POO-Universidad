"""
    programa1
    nombre = gustavo salome
    fecha = 23/01/23
    descripcion = en este codigo se van a conocer los comentarios, 
    multilinea y concateneacion
"""
base = None
altura = None

base = float(input("escriba la base del triangulo: "))
altura = float(input("escribir la altura del triangulo: "))
area = base * altura / 2
print("el area del triangulo es igual: {}".format(area))


lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))
perimetro = lado1 + lado2 + lado3 
print(f"{perimetro} cm")
