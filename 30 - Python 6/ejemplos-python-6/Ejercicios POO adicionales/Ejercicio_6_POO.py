import random

# ----------------- Clase Dado -----------------
class Dado:

    def tirar(self):
        self.valor=random.randint(1,6)

    def imprimir(self):
        print(f'Valor del dado: {self.valor}')

    def retornar_valor(self):
        return self.valor

# ----------------- Clase Juego De Dados ----------------- 
class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        # if (self.dado1.retornar_valor()==self.dado2.retornar_valor() 
        #     and self.dado1.retornar_valor()==self.dado3.retornar_valor()):
        if (self.dado1.retornar_valor()==self.dado2.retornar_valor()==self.dado3.retornar_valor()):
            print("Ganó")
        else:
            print("Perdió")

    def simular_jugadas(self, cantidad):
        self.cantidad = cantidad
        i = 1
        while i <= cantidad:
            self.jugar()
            print()
            i += 1

# ----------------- Bloque principal ----------------- 
juego_dados=JuegoDeDados()
# juego_dados.jugar()
juego_dados.simular_jugadas(20)