from signal import alarm


class Alumno:
    def inicializarse(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    def mostrar_estado(self):
        if self.nota >7:
            print("Estas Aprobado")   
        else:
            print("Lamentablemente estas Desaprobado") 
    
alumno_1 = Alumno()
alumno_1.inicializarse("Jimena", 8)
alumno_1.imprimir()
alumno_1.mostrar_estado()

alumno_2 = Alumno()
alumno_2.inicializarse("Juan", 4)
alumno_2.imprimir()
alumno_2.mostrar_estado()