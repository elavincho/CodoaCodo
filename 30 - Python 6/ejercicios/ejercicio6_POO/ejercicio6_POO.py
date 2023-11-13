''''
Ejercicio 6 (colaboración de clases): Se debe implementar un programa que permita jugar
a un juego de dados. El juego sigue las siguientes reglas:
 Se tiran tres dados al mismo tiempo.
 Si los tres dados muestran el mismo valor, el jugador gana.
 Si no se cumplen las condiciones del punto 2, el jugador pierde.
El programa debe constar de las siguientes partes:
a) Una clase llamada Dado que debe tener los siguientes métodos:
 tirar(): Este método debe generar un valor aleatorio entre 1 y 6 y asignarlo como el
valor del dado.
 imprimir(): Este método debe imprimir el valor actual del dado.
 retornar_valor(): Este método debe devolver el valor actual del dado.
b) Una clase llamada JuegoDeDados que debe tener los siguientes métodos:
 __init__(): Este método debe inicializar tres instancias de la clase Dado como
atributos (dado1, dado2 y dado3).
 jugar(): Este método debe simular una jugada del juego. Para ello, debe tirar los tres
dados, imprimir los resultados y determinar si el jugador ganó o perdió según las
reglas mencionadas anteriormente.
 simular_jugadas(cantidad): Este método debe simular una cantidad especificada de
jugadas del juego. Debe llamar al método jugar() la cantidad de veces especificada
y mostrar los resultados.
Resultado esperado: El programa debe simular 20 jugadas del juego de dados y mostrar los
resultados de cada jugada.
'''
import random

#------------------- Clase Dado--------------------------

class Dado:
    def tirar(self):
        self.valor = random.randint(1,6)

    def imprimir(self):
        print(f"{self.valor}", end=' ')

    def retornar_valor(self):
        return self.valor
    
#-----------------Clase Juego de Dados-------------------

class JuegoDeDados:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

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
            print(" Ganaste!!")
        else:
            print(" Perdiste!")

    def simular_jugadas(self, cantidad):
        self.cantidad = cantidad

        i=1
        while i <= cantidad:
            self.jugar()
            i +=1

#Programa principal

juego_dados = JuegoDeDados()
juego_dados.simular_jugadas(20)



              








