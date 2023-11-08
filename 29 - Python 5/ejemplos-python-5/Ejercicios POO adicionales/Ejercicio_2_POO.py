
class Alumno:
    
    def inicializar(self, nombre, nota): # Constructor
        self.nombre = nombre # Atributo de instancia
        self.nota = nota # Atributo de instancia
    
    def imprimir(self): # Método para mostrar datos
        print(f'{self.nombre} se sacó un {self.nota}')
    
    def mostrar_estado(self): # Método para ver el estado del alumno
        if self.nota >= 7:
            print(f'{self.nombre} promocionó')
        elif self.nota >= 4:
            print(f'{self.nombre} rinde final')
        else:
            print(f'{self.nombre} desaprobó')
        print()

#Programa principal
alumno1 = Alumno() # Creamos el objeto
alumno1.inicializar("Juan", 8)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno() # Creamos el objeto
alumno2.inicializar("Luisa", 4)
alumno2.imprimir()
alumno2.mostrar_estado()

alumno3 = Alumno() # Creamos el objeto
alumno3.inicializar("Diego", 2)
alumno3.imprimir()
alumno3.mostrar_estado()
