"""
    programa1
    nombre = gustavo salome
    fecha = 31/01/23
    descripcion = formulas para sacar el area y perimetro de un 
    circulo
"""
import math 
  
R=float(input("Escribe el radio del circulo :"))# se pide el valor de radio 
 circunferencia=2*math.PI*R #formula para la circunferencia de un circulo 
 area=math.PI*R*R# se hace la operacion para sacar el area del circulo 
 superficiedearea=4*math.PI*R*R# se hace la operacion para sacar la superficie de area 
 print ( "Circunferencia:% .2f" % circunferencia) # imprime  la circunferencia del circulo 
 print ( "Area del circulo:% .2f"% area) # imprimer el resultado del area del circulo 
 print ( "Area de superficie del circulo:% .2f"%superficiedearea)# se imprime el resultado de la superficie del circulo