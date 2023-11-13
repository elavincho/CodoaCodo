class Materia:

    # Constructor de clase
    def __init__(self, codigo, nombre, duracion):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        print(f'Se ha creado la materia: {self.codigo}-{self.nombre}')

    def __str__(self):
        if self.duracion == 4:
            durac = "Cuatrimestral"
        elif self.duracion == 8:
            durac = "Anual"
        else:
            durac = "A confirmar"

        return f'{self.codigo}: {self.nombre} ({durac})'

class Carrera:

    materias = []  # Esta lista contendrá objetos de la clase Materia

    def __init__(self, nombre, materias=[]):
        self.nombre = nombre
        self.materias = materias

    def agregar(self, mat):  # mat será un objeto Materia
        self.materias.append(mat)

    def __str__(self):
        linea = "="*60
        cad = f'\n{linea}\n{self.nombre.upper()} - Listado de materias:\n'
        for i in range(len(self.materias)):
            cad = cad + str(self.materias[i]) + "\n"
        cad = cad + linea + "\n"
        return cad

#Programa principal

materia1 = Materia("A1000", "Algoritmos I", 4) #Creamos nuestra primera materia
print(materia1)

carrera1 = Carrera("Licenciatura en Python", [materia1])  # Instanciamos la carrera con una materia
print(carrera1) # Imprimimos la carrera con una materia

# Agregamos 3 materias
carrera1.agregar(Materia("A1001", "Python I", 8))  # Añadimos otra materia
carrera1.agregar(Materia("A1002", "Objetos I", 6))  # Añadimos otra materia
carrera1.agregar(Materia("A1003", "Inteligencia Artificial", 4))  # Añadimos otra materia

print(carrera1) # Imprimimos la carrera con más materias
print()