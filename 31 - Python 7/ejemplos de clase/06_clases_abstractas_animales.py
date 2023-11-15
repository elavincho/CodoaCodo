



from abc import ABC, abstractmethod

# Acá lo que creamos es una interfaz, es decirle qué métodos va a tener la clase
# No sabemos cómo va a ser implementado porque no todos los animales se comportan igual
# No tengo forma de implementar esta clase

class Animal(ABC): #Creamos la clase abstracta con métodos abstractos
    @abstractmethod #Indicamos que va a ser un método abstracto
    def mover(self):
        pass #El pass define que sólo crea el método, la estructura pq luego cada subclase le va a asignar su valor

    @abstractmethod #Indicamos que va a ser un método abstracto
    def emitir_sonido(self):
        print("El animal emite sonido: ", end="")
    
# Este es un modelo para construir algo más, pero no va a poder ser implementado
# Porque no conozco del todo el comportamiento de esa clase

class Gato(Animal): #Creo la clase Gato que hereda de Animal

    def mover(self): #Le doy al método abstracto un comportamiento particular
        print("El gato se sube al techo.")

    def emitir_sonido(self): # Sobreescribo el método abstracto
                             # Agregándole comportamiento al método anterior
        super().emitir_sonido() # Aprovecho la superclase animal y llamo a su comportamiento
        print("Miau!") # Le agrego algo propio

class Perro(Animal): #Creo la clase Perro que hereda de Animal

    def mover(self): #Le doy al método abstracto un comportamiento particular
        print("El perro está corriendo.")

    def emitir_sonido(self): #Sobreescribo el método abstracto
                             #Agregándole comportamiento al método anterior
        super().emitir_sonido() #Aprovecho la superclase animal y llamo a su comportamiento
        print("Guau, Guau!") #Le agrego algo propio


#Programa principal
animal1 = Gato() # Instancia del objeto Gato, ya no tengo el constructor
animal1.mover() # Llamo al método 
animal1.emitir_sonido() # Llamo al método

animal2 = Perro() # Instancia del objeto Gato, ya no tengo el constructor
animal2.mover() # Llamo al método
animal2.emitir_sonido() # Llamo al método
