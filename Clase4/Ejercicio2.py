#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final. Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

inicio, final = 10, 20

for i in range(inicio, final +1):
    if i % 2 !=0:
        print(i)
    