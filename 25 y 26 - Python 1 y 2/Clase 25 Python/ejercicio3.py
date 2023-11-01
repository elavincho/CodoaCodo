'''
Ejercicio 3: La universidad requiere un programa para organizar las aulas para los alumnos de primer año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los días cuyo número de orden son pares los alumnos cursan en el aula A-300, mientras que aquellos días impares cursan en el aula A-315.
Además se requiere un programa que otorgue un descuento especial del 25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y se inscriban a más de 3 materias, para el resto de los casos el descuento será de un 5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
También se requiere que el programa asigne un costo diario de estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50 si vienen en bicicleta.
'''

# dia = int(input("Ingrese el número del día (1 = Lunes / 6 = Sábado): "))

# print("=================Aulas===================")
# if dia % 2 == 0:
#     aula = "A-300"
# else:
#     aula = "A-315"

# print("Aula: ", aula)

print()
print("=======Descuento y Estacionamiento=======")

turno = input("Ingrese el Turno(Mañana/Tarde/Noche): ")
materia = int(input("Ingrese la Cantidad de Materias: "))
vehiculo = input("Ingrese el Tipo de Vehiculo en el que Ingresa(Auto-Moto-Bicicleta): ")
cuota = 10000

if turno == "Tarde" and materia > 3:
    cuota = cuota - (cuota*0.25)
else:
    cuota = cuota - (cuota*0.05)

print("El valor de la cuota es: ", cuota)

if vehiculo == "Auto" or vehiculo == "Moto":
    costo_estacionamiento = 300
else:
    costo_estacionamiento = 50

print("El Costo de Estacionamiento: ", costo_estacionamiento)










       






