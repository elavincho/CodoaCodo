#Herencia Multiple

class Padre(): #Superclase
    def __init__(self):
        self.apellido = "Pérez"

    def llevar(self):
        print(f"Mi papa me lleva al colegio.")

    def programar(self):
        print(f"Papá programa en JAVA.")

class Madre():
    def __init__(self):
        self.apellido = "Osorio"

    def retirar(self):
        print(f"Mamá me retira del colegio.")

    def programar(self):
        print(f"Mi mamá programa en Python.")


class Hijo(Madre, Padre): #Depende del orden que coloque va a acceder a los atributos
    nombre = ""


    def jugar(self):
        print(f"Soy {self.nombre} {self.apellido} y juego al voley.")


#Programa principal

hijo1 = Hijo()
hijo1.nombre = "Fernando"
hijo1.jugar()
hijo1.llevar()
hijo1.programar()
hijo1.retirar()