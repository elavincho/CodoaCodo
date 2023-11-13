class Perro:
    # Atributo de Clase
    genero= "Canis"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método de instancia
    def imprimir(self):
        return f'{self.nombre} tiene {self.edad} años.'
    # Otro método de instancia
    def ladrar(self, sonido):
        return f'{self.nombre} dice {sonido}.'

    # Se puede reemplazar el método imprimir() con __str__()
    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años.'

miMascota = Perro("Paka", 11)
miMascota.imprimir()
miMascota.ladrar("Guau guau!")

print("Género:", miMascota.genero)
print(miMascota.imprimir())
print(miMascota.ladrar("Guau, guau!"))
print(miMascota)


