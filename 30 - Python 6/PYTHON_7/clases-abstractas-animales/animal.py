from abc import ABC, abstractmethod

#Acá lo que creamos es una interfaz, es decirle qué métodos va a tener la clase
#No sabemos cómo va a ser implementado porque no todos los animales se comportan igual
# No tengo forma de implementar esta clase

class Animal(ABC): #Creamos la clase abstracta con métodos abstractos
    @abstractmethod #Indicamos que va a ser un método abstracto
    def mover(self):
        pass

    @abstractmethod #Indicamos que va a ser un método abstracto
    def emitir_sonido(self):
        print("Animal emite sonido: ", end="")
    
# Este es un modelo para construir algo más, pero no va a poder ser implementado
# Porque no conozco del todo el comportamiento de esa clase