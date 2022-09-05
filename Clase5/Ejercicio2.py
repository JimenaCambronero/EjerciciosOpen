#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def primo(num):
    if num == 0 or num == 1 or num == 4:
        return False
    for x in range(2, int(num/2)):
        if num % x == 0:
            return False
    return True

num = int(input('ingrese un número para saber si es primo: '))
es_primo = primo(num)  
if es_primo:
        print('El número ingresado es primo')
else: 
    print ('el numero ingresado No es primo')
    