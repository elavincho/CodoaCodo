# Polimorfismo
# Fuente: https://www.youtube.com/watch?app=desktop&v=kV1cN_bqcSw
# Poli = Muchas; Morfo: Formas
# El polimorfismo es la capacidad que tienen los objetos en diferentes clases
# para usar un comportamiento o atributo del mismo nombre pero con diferente valor
'''
Un objeto puede cambiar de forma dependiendo del contexto en el que se utiliza.
Al cambiar de forma ese mismo objeto también cambia de comportamiento.
Si hablamos de vehículos, un mismo objeto puede cambiar de forma (pasar de ser un camión,
una moto o un auto) y por lo tanto cambiaría de comportamiento dependiendo del contexto
en que se encuentre.
Dado que Python es un lenguaje de programación de tipado dinámico no necesitamos especificar
de qué tipo es un objeto a la hora de utilizarlo, simplificando las cosas.

'''

# Crearemos 3 clases con el mismo método, pero cada una tendrá un comportamiento diferente
class Auto:
    def desplazarse(self):
        print("Me desplazo utilizando cuatro ruedas.")

class Moto:
    def desplazarse(self):
        print("Me desplazo utilizando dos ruedas.")

class Camion:
    def desplazarse(self):
        print("Me desplazo utilizando seis ruedas.")

#Programa principal (sin polimorfismo)
#Utilizamos el mismo método/comportamiento, pero pertenece a clases diferentes

# vehiculo1 = Auto() #Instancia de la clase Auto
# vehiculo1.desplazarse() #Método del objeto

# vehiculo2 = Moto() #Instancia de la clase Moto
# vehiculo2.desplazarse() #Método del objeto

# vehiculo3 = Camion() #Instancia de la clase Camion
# vehiculo3.desplazarse() #Método del objeto
 



# Si crearamos un juego con diferentes autos, bicicletas, triciclos, camiones, etc
#Cada uno de ellos tendrá su propio método desplazarse
#Si quisiéramos utilizar en ese juego cada uno de los objetos tendríamos que hacerlo uno por uno
#Gracias al polimorfismo podremos hacer lo siguiente:


def moverse(vehiculo): #Recibe un objeto como parámetro, no sabemos de qué tipo es, no tenemos que especificarlo: ¿a qué método desplazarse llamará, a cuál de los tres?
    vehiculo.desplazarse()


#Programa principal (empleando polimorfismo)
#Gracias al polimorfismo, como un objeto puede tener la capacidad de cambiar de forma y de comportarse de diferente forma dependiendo del contexto va a saber en todo momento a que método desplazarse tiene que llamar:

miVehiculo=Camion() #Podemos cambiarlo por Auto() o Moto()
moverse(miVehiculo)
moverse(Moto()) #El objeto puede cambiar de forma
moverse(Auto()) #El objeto puede cambiar de forma

