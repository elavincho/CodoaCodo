class Vehiculo(): #Superclase 

    def __init__(self, color, ruedas):
        self.color = color #Atributos de instancia
        self.ruedas = ruedas #Atributos de instancia

    def __str__(self):
        return f'Color: {self.color}\nRuedas: {self.ruedas}'

    def andar(self):
        print(f'Estoy andando en {self.ruedas} ruedas')

class Transporte(Vehiculo):
    def __init__(self, color, ruedas, velocidad, modelo):
        Vehiculo.__init__(self, color, ruedas) #Atributos heredados
        self.velocidad = velocidad #Atributos propios
        self.modelo = modelo #Atributos propios

    def __str__(self):
        return Vehiculo.__str__(self) + f'\nVelocidad: {self.velocidad} km/h\nModelo: {self.modelo}' #Muestra atributos heredados y atributos propios

# Programa principal
vehiculo1 = Vehiculo("Rojo", 2) #Instancia del padre
print(vehiculo1)
vehiculo1.andar()
print()
coche1 = Transporte("Azul", 4, 150, "Ford") #Instancia del hijo
print(coche1)
coche1.andar()
print()
moto1 = Transporte("Rojo", 2, 220, "Yamaha") #Instancia del hijo
print(moto1)
moto1.andar()