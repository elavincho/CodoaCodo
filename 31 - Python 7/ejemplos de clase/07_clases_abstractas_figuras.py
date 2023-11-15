# Clases abstractas
# Fuente: https://www.youtube.com/watch?v=H9SnCQvoNHk



import math
from abc import ABC, abstractmethod

class Figura(ABC): #Clase abstracta
#Las clases que hereden de figura están obligadas a cumplir con ese contrato de implementación, deben sí o sí implementar area y perimetro (métodos abstractos)

    #Métodos abstractos
    @abstractmethod
    def area(self):
        pass #Método abstracto: no hay implementación, cuerpo de declaración vacío
    
    @abstractmethod
    def perimetro(self):
        pass #Método abstracto: no hay implementación, cuerpo de declaración vacío

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

#Programa principal
print("Rectángulo: área y perímetro")
r = Rectangulo(3,5)
print(r.area())
print(r.perimetro())
print()

print("Círculo: área y perímetro")
c = Circulo(5)
print(c.area())
print(c.perimetro())

figu = Figura()

# Las clases abstractas no son instanciables (no se pueden crear objetos de una clase abstracta)
