'''
Ejercicio 5 (colaboración de clases): El comedor de la universidad tiene un sistema de
beneficios a través del cual los alumnos pueden sumar puntos o canjearlos por menús. El
comedor necesita al final del día un reporte de la cantidad de puntos que sus alumnos
poseen. Crear 3 alumnos cuyos atributos son su nombre y la cantidad de puntos que poseen,
inicializado en 0. Crear un método que simule las operaciones de ingresar puntos y de
canjear puntos.
'''
#------------------------- Clase Alumno-----------------------
class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def __str__(self):
        return f"{self.nombre}\t\t{self.puntos} puntos."
    
    def ingresar_puntos(self, puntos):
        self.puntos += puntos

    def canjear_puntos(self, puntos):
        self.puntos -= puntos

    def retornar_puntos(self)  :
        return self.puntos

#------------------ Clase Comedor-----------------------------

class Comedor:

    def __init__(self, sede):
        self.sede = sede
        self.alumno1 = Alumno("Juan")
        self.alumno2 = Alumno("Luciana")
        self. alumno3 = Alumno("Sofia")

    def __str__(self):
        return f"{'-'*30}\n{self.sede}\n{'-'*30}\n"
    
    def operaciones(self): #simular movimientos
        self.alumno1.ingresar_puntos(100)
        self.alumno2.ingresar_puntos(200)
        self.alumno3.ingresar_puntos(150)

        self.alumno3.canjear_puntos(50)
        self.alumno1.canjear_puntos(100)
        self.alumno2.canjear_puntos(100)

        self.alumno1.ingresar_puntos(300)

    def puntos_totales(self):
        print("Detalle de puntos del día: ")
        print(self.alumno1)
        print(self.alumno2)
        print(self.alumno3)
        print("-"*30)
        total = self.alumno1.retornar_puntos() + self.alumno2.retornar_puntos() + self.alumno3.retornar_puntos()
        print(f"Total\t\t {total} puntos.")


#Programa principal
comedor1 = Comedor("El comedor de la Universidad")
print(comedor1)
comedor1.operaciones()
comedor1.puntos_totales()











