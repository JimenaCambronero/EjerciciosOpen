#Escribe un programa que pregunte la edad al usuario y muestre en pantalla si es mayor o no

edad = int(input ('Ingresa tu edad: '))

if edad >18:
    print (f'Tu edad es de {edad}, ya eres mayor de edad')
else:
    print('Eres menor de edad, disfruta tu juventud')