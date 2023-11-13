'''
Ejercicio 7 (variables de clase): Se debe implementar una clase Alumno que almacene la
información de un estudiante, incluyendo un código de alumno, un nombre y su nota final
en una materia. Además, la clase Alumno debe mantener dos listas de variables de clase,
una de ellas llamada aprobados, que almacenará los códigos de los alumnos aprobados
(nota mayor o igual a 4) y otra llamada reprobados que almacenará los códigos de los
alumnos reprobados (nota menor a 4).
La clase Alumno debe tener los siguientes métodos:
 __init__(self, codigo, nombre, nota): Este método inicializa un objeto de tipo Alumno
con el código, nombre y nota proporcionados. Además, invoca el método
definir_estado() para determinar si el alumno está aprobado o reprobado.
 __str__(self): Este método devuelve una representación en forma de cadena del objeto
Alumno, que incluye el código, nombre y nota.
 definir_estado(self): Este método determina si el alumno está aprobado o reprobado,
y actualiza las listas aprobados y reprobados en consecuencia.
A continuación, crear cuatro objetos de tipo Alumno con notas distintas y almacenarlos en
una lista. Posteriormente, mostrar los datos de los 4 alumnos y finalmente mostrar la lista
de los códigos de los alumnos aprobados y además los códigos de los alumnos reprobados,
uno debajo del otro.

'''

class Alumno:
    aprobados = []
    reprobados = []

    def __init__(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota

        #método definir estado
        Alumno.definir_estado(self)


    def __str__(self):
        return f"{self.codigo}\t{self.nombre}\t{self.nota}"
    
    def definir_estado(self):
        if self.nota >= 4:
            Alumno.aprobados.append(self.codigo)
        else:
            Alumno.reprobados.append(self.codigo)

    
#Programa principal

alumno1 = Alumno(100, "Juan", 3)
alumno2 = Alumno(101, "Ana", 6)
alumno3 = Alumno(102, "Diego", 2)
alumno4 = Alumno(103, "Roxana", 10)

print("Legajo\tNombre\tNota")
print(alumno1)
print(alumno2)
print(alumno3)
print(alumno4)


print(f"Aprobados: {Alumno.aprobados}")

print("Reprobados: ")
for i in range(len(Alumno.reprobados)):
    print(Alumno.reprobados[i])















