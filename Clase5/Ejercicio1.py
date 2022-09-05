#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros 

import math

def calcular_area_triangulo (base,altura):
    return base * altura /2

print(calcular_area_triangulo (5,10))

#calcule el área de un círculo recibiendo el radio del mismo.

def area_circulo(radio): 
    return math.pi *radio **2

print (area_circulo(8))