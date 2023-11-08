class Animal:

    def __init__(self, nombre, tipo, edad): # Permite instanciar y agregar valores a los atributos
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    
    def imprimir(self):
        print(f'Tipo: {self.tipo}\nNombre: {self.nombre}\nEdad: {self.edad} años.')

    def __str__(self): # Reemplaza al método imprimir
        return f'Tipo: {self.tipo}\nNombre: {self.nombre}\nEdad: {self.edad} años.'

    def __del__(self): # Elimina el objeto
        print(f'{self.nombre} ha sido eliminado')

# Programa principal
mi_animal1 = Animal("Lassie", "Perro", 11)
# mi_animal1.imprimir()
print(mi_animal1)

print()
mi_animal2 = Animal("Dumbo", "Elefante", 35)
print(mi_animal2)
# del mi_animal2





