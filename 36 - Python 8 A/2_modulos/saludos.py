def saludar():
    print("Hola, te estoy saludando desde la función saludar()")

def saludar_dos(nombre):
    print(f'Hola {nombre}!')

def saludar_tres(ciudad):
    print(f'La ciudad es {ciudad},', end=" ")
    temperatura(35)

def temperatura(temp):
    print(f'y la temperatura es {temp} °C.')

class Saludo:
    def __init__(self, ape, nom):
        self.apellido = ape
        self.nombre = nom
        print(f'Hola {self.nombre} {self.apellido}, te doy la bienvenida desde el __init__ de la clase Saludo')
