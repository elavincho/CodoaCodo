class Alumno:
    aprobados = []
    reprobados = []
                   
    def __init__(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota
        Alumno.definir_estado(self)

    def __str__(self):
        return f'{self.codigo}\t{self.nombre}\t{self.nota}'

    def definir_estado(self):
        if self.nota >= 4:
            Alumno.aprobados.append(self.codigo)
        else:
            Alumno.reprobados.append(self.codigo)

# Programa principal
alumno1=Alumno(1,"Juan",5)
alumno2=Alumno(2,"Ana",2)
alumno3=Alumno(3,"Diego",9)
alumno4=Alumno(4,"Pedro",3)

print("Legajo\tNombre\tNota")
print(alumno1)
print(alumno2)
print(alumno3)
print(alumno4)

#Dos formas de mostrar la información
print(f'Aprobados: {Alumno.aprobados}')

print("Reprobados:")
for i in range(len(Alumno.reprobados)):
    print(Alumno.reprobados[i])