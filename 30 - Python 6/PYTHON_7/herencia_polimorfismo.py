class Vehiculo():

    def __init__(self, color, ruedas):
        self.color= color
        self.ruedas= ruedas
    
    def __str__(self):
        return "Color: {} - Ruedas: {}".format(self.color, self.ruedas)
    
# Herencia (simple: de una única superclase)
class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad): #Constructor de la clase auto 
                                                  #Se colocan color y ruedas porque derivan de la clase vehículo
        # Vehiculo.__init__(self, color, ruedas) # Llamada al método constructor de la superclase 
        super().__init__(color, ruedas) #Invocamos al constructor de la superclase (reemplaza a lo de arriba)
        self.velocidad= velocidad

    # sobreescritura del método especial/mágico str
    def __str__(self):
        return super().__str__() + " - Velocidad: " + str(self.velocidad) #le agregamos la velocidad

# Programa principal
v1= Vehiculo("Blanco",2)
a1= Auto("Rojo",4,140)
a2= Auto("Negro",4,180)
a3= Auto("Azul",4,200)

print(v1)
print(a1)
print(a2)
print(a3)

vehiculos= []
vehiculos.append(v1)
vehiculos.append(a1)
vehiculos.append(a2)
vehiculos.append(a3)

#Polimorfismo
print(vehiculos[0])
print(vehiculos[2])

# Muestro todos los Vehículos (Vehículo o Auto)
print("Listado de vehículos: ")
for Vehiculo in vehiculos:
    print(Vehiculo)