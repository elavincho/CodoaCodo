import random

# ----------------- Clase Dado -----------------
class Dado:

    def tirar(self):
        self.valor = random.randint(1,6)

    def imprimir(self):
        print(f'{self.valor}', end=' ')

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

        valor_dado1 = self.dado1.retornar_valor()
        valor_dado2 = self.dado2.retornar_valor()
        valor_dado3 = self.dado3.retornar_valor()
        
        if valor_dado1 == valor_dado2 and valor_dado1 == valor_dado3:
            print("Ganó")
        else:
            print("Perdió")

    def simular_jugadas(self, cantidad):
        self.cantidad = cantidad
        i = 1
        while i <= cantidad:
            self.jugar()
            i += 1

# ----------------- Bloque principal ----------------- 
juego_dados=JuegoDeDados()
#juego_dados.jugar()
juego_dados.simular_jugadas(20)