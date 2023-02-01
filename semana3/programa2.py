radio = None
pi = 3.1416

while True:
  try:
    radio = float(input("escriba el radio del circulo"))
    break
  except:
    print("debe escribir un numero")

while True:
  try:
    pi = float(input("escribir pi."))
    break
  except:
    print("debe escribir un numero.")

area = pi * (radio **2)
print("el area del circulo es igual: {}".format (area))

valor = 2
radio = None
pi = 3.1416
while True:
  try:
    pi = float(input("escribir pi."))
    break
  except:
    print("debe escribir un numero")

while True:
  try:
    radio = float()