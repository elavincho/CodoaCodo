'''
Implementar una clase llamada Empleado, que posee un atributo de clase (nro_empleados) que lleva la cuenta de los objetos instanciados.
Cada objeto de la clase Empleado posee un legajo, nombre completo y un sueldo.
Definir métodos para inicializar sus atributos, definir su categoría (variable de clase), procesar su eliminación de la memoria y para mostrar un texto con la categoría asignada.
La categoría es "Full Time" para los legajos comenzados en "F", "Part time" para los legajos comenzados en "P" y "Contratado" para los comenzados en "C", para el resto la categoría es vacía.
En el programa principal instanciar distintos objetos de la clase Empleado y mostrar sus características encolumnadas. Al salir del programa eliminarlos de la memoria.
'''

class Empleado:  # Creamos la clase
    nro_empleados = 0  # Cantidad de empleados
    categoria = ""

    # Constructor
    def __init__(self, legajo, nombreCompleto, sueldo):
        self.legajo = legajo
        self.nombreCompleto = nombreCompleto
        self.sueldo = sueldo
        Empleado.nro_empleados += 1  # Agregamos un empleado

    # Mostrar datos del objeto
    
    def __str__(self):
        inicial_legajo = self.legajo[0] #Primera inicial del legajo

        if inicial_legajo == "F":
            self.categoria = "Full Time"
        elif inicial_legajo == "P":
            self.categoria = "Part time"
        elif inicial_legajo == "C":
            self.categoria = "Contratado"

        cadena = f'{self.legajo}\t{self.nombreCompleto}\t{self.sueldo}\t{self.categoria}'
        
        return cadena

    def titulos():
        print(f'Legajo\tNombre Completo\tSueldo\tCategoria')

    # Damos de baja al empleado
    def __del__(self):
        Empleado.nro_empleados -= 1  # Restamos un empleado
        print(f'{self.nombreCompleto} ha sido dado de baja - Restan: {Empleado.nro_empleados}')
      

# Programa principal
emp1 = Empleado("F1000", "Juan Pérez", 150000)
emp2 = Empleado("P1001", "Ana Gómez", 240000)
emp3 = Empleado("C1002", "Luciano García", 130000)
emp4 = Empleado("H1003", "Marcela Priore", 220000)

Empleado.titulos()
print(emp1)
print(emp2)
print(emp3)
print(emp4)
print()
input("Pulse Enter para salir: ")
print()
del emp1
print(emp1)

