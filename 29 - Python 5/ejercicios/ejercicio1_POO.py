'''
Ejercicio 1: Implementar una clase llamada Estudiante que tendrá como atributos
(variables) su nombre, su apellido, dni y dos métodos (funciones), uno de dichos métodos
inicializará los atributos y el siguiente método los mostrará en pantalla. Definir dos objetos
de la clase Estudiante e incorporar una variable de clase (piernas).


'''


class Estudiante:

    hijos = 2

    def inicializar(self, nombre, apellido, dni): #Metodo constructor
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni



    def imprimir(self):
        print(f"Apellido y Nombre: {self.apellido.upper()}, {self.nombre}\nDNI: {self.dni}")
        

#Programa principal
est1 = Estudiante() #Instanciamos un objeto de la clase estudiante
est1.inicializar("Pepe", "Argento", 12345678)
est1.imprimir()

est2 = Estudiante()
est2.inicializar("Lucia", "Perez", 87456123)
est2.imprimir()

print(f"Los estudiantes tienen {Estudiante.hijos} hijos.")
print(f"{est1.nombre} tiene {est1.hijos} hijos.")
print(f"{est2.nombre} tiene {est2.hijos} hijos.")

est1.hijos = 4
print(f"{est1.nombre} tiene {est1.hijos} hijos.")

est2.nombre = "Fernanda"
print(f"{est2.nombre}")

est1.edad = 37
print(f"{est1.edad}")



