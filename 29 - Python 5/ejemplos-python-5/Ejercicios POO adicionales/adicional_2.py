class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion: "))
            if opcion==1: 
                self.cargar()
            elif opcion==2: 
                self.listar()
            elif opcion==3: 
                self.notas_altas()
            elif opcion==4: 
                self.finalizar()
            else: 
                print("Opción no válida!")

    def cargar(self):
        for x in range(5):
            nombre=input("Ingrese nombre del alumno: ")
            self.nombres.append(nombre)
            nota=int(input("Nota del alumno: "))
            self.notas.append(nota)

    def listar(self):
        print("Listado completo de alumnos")
        print(f'Alumno\tNota')
        for x in range(5):
            print(f'{self.nombres[x]}\t{self.notas[x]}')
        print()

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        print(f'Alumno\tNota')
        for x in range(5):
            if self.notas[x]>=7:
                print(f'{self.nombres[x]}\t{self.notas[x]}')
        print()    

    def finalizar(self):
        print("Adiós!")
        print()

# Bloque principal
alumnos=Alumnos()
alumnos.menu()
