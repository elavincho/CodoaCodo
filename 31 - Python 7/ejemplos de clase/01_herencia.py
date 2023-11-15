class Padre(): #SuperClase
    def __init__(self):
        self.apellido = "Argento"

    def hacer_deporte(self):
        print(f"Estoy haciendo deporte.")


class Hijo(Padre): #Subclase que extiende de la clase padre
    nombre = ""

    def jugar(self):
        print(f"Soy {self.nombre} y estoy jugando al futbol.")


#Programa principal

hijo1 = Hijo() #creamos un objeto
hijo1.nombre = "Coqui"

hijo1.hacer_deporte() #metodo del padre
hijo1.jugar() #metodo propio de la clase hijo

#Imprimimos atributos heredados del padre y propios

print(f"El hijo se llama {hijo1.nombre} {hijo1.apellido}")


