class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return " Mi autos es de color {}, tiene {} ruedas y {} puertas.".format(self.color, self.ruedas, self.puertas)
         
        
class Coche (Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + " Su velocidad maxima es de {} km/h y tiene {} cc de cilindrada".format( self.velocidad, self.cilindrada)
    

auto = Coche("amarillo", 4, 4, 240, 200)
print(auto)
         
        
        
    


    