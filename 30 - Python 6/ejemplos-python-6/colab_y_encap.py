# Colaboración y encapsulación
'''
Crear una clase Carrera, que tenga un método constructor y otro que
permita agregar materias a la carrera.
Crear otra clase, Materia, que tenga los atributos privados nombre,
profesor y fecha_inicio. Proporcionar un método para acceder a la
fecha_inicio.

'''

# ---------------- Clase MATERIA ----------------

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        #Fecha no puede ser anterior a 2006
        self.fechaInicio = fecha

    @property
    def fecha_inicio(self):
        # print("Estoy obteniendo la fecha de inicio")
        return self.__fechaInicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha):
        # print("Estoy seteando la fecha de inicio")
        if fecha < 2006:
            self.__fechaInicio = 2006
        else:
            self.__fechaInicio = fecha

# ---------------- Clase CARRERA ----------------
class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        #Contendrá tuplas (código, materia)
        self.materias = {}
    
    # Este método agrega materias a la    
    # colección de materias
    def agregar_materia(self, materia, codigo):
        self.materias[codigo] = materia

# ---------------- PROGRAMA PRINCIPAL ----------------

#Creamos una carrera y tres materias
carrera1 = Carrera("Ingeniería en Sistemas")
algebra = Materia("Algebra", "Juan Quinteros", 2004)
fisica = Materia("Física", "Pedro Perez", 2012)
programacion = Materia("Programación", "Lorena Ríos",2022)
#Agregamos las materias a la carrera:
carrera1.agregar_materia(201,algebra)
carrera1.agregar_materia(202,fisica)
carrera1.agregar_materia(203,programacion)
# Veomos la fecha de inicio de dictado de algunas materias:
print(f"La fecha de inicio de {algebra.nombre} es {algebra.fechaInicio}")
print(f"La fecha de inicio de {fisica.nombre} es {fisica.fechaInicio}")
print(f"La fecha de inicio de {programacion.nombre} es {programacion.fechaInicio}")