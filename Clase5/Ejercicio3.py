def es_bisiesto(anio):
  if type(anio) is not int:
    print('Debes ingresar un numero entero mayor a 1852')
  elif anio %4 == 0 and (anio %100 != 0 or anio % 400 == 0):
    print(f'El año {anio} es bisiesto.')
  else: 
    print(f'El año {anio} no es bisiesto.')
 
  
es_bisiesto(1900)
es_bisiesto (2000)
es_bisiesto ('Holi no soy un numero')    

