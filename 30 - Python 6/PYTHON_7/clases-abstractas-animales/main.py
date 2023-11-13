from gato import Gato
from perro import Perro

# Bloque Ppal
def __main__():  #Este método es el método principal donde programo mi programa principal
    g1= Gato() #Instancia del objeto Gato, ya no tengo el constructor
    g1.mover() #Llamo al método
    g1.emitir_sonido() #Llamo al método
    p1= Perro()
    p1.mover()
    p1.emitir_sonido()

if __name__ == "__main__": #En este caso compruebo que tengo el método main
    __main__() #Si está llamo al método
               #Si no es así estoy ejecutando el main desde otro módulo