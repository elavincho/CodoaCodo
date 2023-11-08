'''
Ejercicio 2: Implementar una nueva clase llamada Estudiante. Esta clase tendrá como
atributos su nombre y su nota. Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje que indique: “Promocionó” (nota >= 7), “Rinde final”
(nota >= 4) o “Desaprobó”.
Definir tres objetos de la clase Alumno, cada uno con una condición de aprobación
distinta.
'''

class Alumno:
    def inicializar(self, nombre_completo, nota): #Metodo constructor
        self.nombre_completo = nombre_completo
        self.nota = nota

    def imprimir(self):
        print(f"Nombre Completo: {self.nombre_completo} - Nota: {self.nota}")
        
        if self.nota >= 7:
            print("Promocionó")
        elif self.nota >= 4:
            print("Rinde Final.")
        else:
            print("Desaprobó")
        print()


#Programa Principal
estudiante1 = Alumno() #Creamos el objeto
estudiante1.inicializar("Juan Serrano", 8)
estudiante1.imprimir()

estudiante2 = Alumno() #Creamos el objeto
estudiante2.inicializar("Luisa López", 5)
estudiante2.imprimir()

estudiante3 = Alumno() #Creamos el objeto
estudiante3.inicializar("Paola Argento", 2)
estudiante3.imprimir()




















