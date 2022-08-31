#Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:Nombre-Apellidos-Edad-Email-Teléfono-Casado (verdadero o falso)- Con Hijos (verdadero o falso)- Lista de amigos-Películas vistas (diccionario con clave y valor. El valor será el título de la película).
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().

nombre = 'Juan'

apellido = 'Perez'

edad = 24

mi_correo = 'juanperez@hotmail.com'

mi_telefono = 345234
print(f'Mi nombre es {nombre} y mi apellido es {apellido}, tengo {edad} años de edad. Mi dirección de correo electronico es {mi_correo}. Mi número de telefono es {mi_telefono}')

casado = input('Si esta casado ingrese casado si esta soltero ingrese soltero: ')
if casado:
    print(True)
else: print(False)
 
hijosi = input('Tiene hijos s/n: ')
if hijosi:
    print(True)
else: print(False)

amigos = ['Juan', 'Ana', 'Maria','Pedro']
print(amigos)

pelis = {'peli_1': 'duro de matar', 'peli_2':'la muerte le sienta bien', 'peli_3': 'la vida es bella'}
print(pelis)