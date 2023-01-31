base = None
altura = None

while True:
  try:
    base = float(input("escriba la base del triangulo: "))
    break
  except:
    print("debe escribir un numero.")

while True:
  try:
    altura = float(input("escribir la altura del triangulo"))
    break
  except:
    print("debe escribir un numero.")

area = base * altura / 2
print("el area del triangulo es igual: {}".format(area))

lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))
perimetro = lado1 + lado2 + lado3 
print(f"{perimetro} cm")
