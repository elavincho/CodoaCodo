# ------------------------- Clase Alumno -------------------------
class Alumno:

    def __init__(self,nombre):
        self.nombre = nombre 
        self.puntos = 0

    def ingresar_puntos(self,puntos):
        self.puntos = self.puntos + puntos

    def canjear_puntos(self,puntos):
        self.puntos = self.puntos - puntos

    def retornar_puntos(self):
        return self.puntos

    def __str__(self):
        return f'{self.nombre}\t\t{self.puntos} pts.'

# ------------------------- Clase Comedor -------------------------
class Comedor:

    def __init__(self, sede):
        self.sede = sede
        self.alumno1=Alumno("Juan")
        self.alumno2=Alumno("Luciana")
        self.alumno3=Alumno("Sofía")

    def __str__(self):
        return f'{"-"*30}\n{self.sede}\n{"-"*30}\n'

    def operar(self): #simula movimientos
        self.alumno1.ingresar_puntos(100)
        self.alumno2.ingresar_puntos(150)
        self.alumno3.ingresar_puntos(200)
        self.alumno3.canjear_puntos(150)
        self.alumno1.ingresar_puntos(300)
        self.alumno1.canjear_puntos(75)

    def puntos_totales(self):
        print("Detalle de puntos del día:")
        print(self.alumno1)
        print(self.alumno2)
        print(self.alumno3)
        print("-"*30)
        total = self.alumno1.retornar_puntos() + self.alumno2.retornar_puntos() + self.alumno3.retornar_puntos()
        print(f'Total\t\t{total} pts.')

# ------------------------- Programa principal -------------------------
comedor1 = Comedor("El comedor de la Universidad")
print(comedor1)
comedor1.operar()
comedor1.puntos_totales()