# Herencia y polimorfismo
# Fuente: https://www.youtube.com/watch?v=gDGdRXLbFKs

class Animales:
    def __init__(self, nombre, alimento):
        self.nombre = nombre
        self.alimento = alimento

    def tipo_animal(self):
        pass
        
    def alimentarse(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print(f'{self.nombre} es un animal salvaje.')

    def alimentarse(self):
        print(f'{self.nombre} caza {self.alimento} y se los come.')

class Perro(Animales):
    def tipo_animal(self):
        print(f'{self.nombre} es un animal doméstico.')

    def alimentarse(self):
        print(f'{self.nombre} come {self.alimento}.')

#Programa principal 

nuevo_animal = Leon("Simba","antílopes")
nuevo_animal.tipo_animal() #mostrará lo que le corresponde a la clase (polimorfismo)
nuevo_animal.alimentarse()
print()

nuevo_animal2 = Perro("Lassie","Alimento balanceado")
nuevo_animal2.tipo_animal() #mostrará lo que le corresponde a la clase (polimorfismo)
nuevo_animal2.alimentarse()