'''
Ejercicio 2: 
La universidad ahora pide un programa que permita cargar las notas de dos exámenes y obtener el promedio. Además deberá determinar si el alumno aprobó el último examen (nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre ambos parciales.
Para ello se deberá informar "Mejoró su desempeño" si la nota del segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar.
'''

nota1 = float(input("Ingrese la Nota del Primer Parcial: "))
nota2 = float(input("Ingrese la Nota del Segundo Parcial: "))
promedio = ((nota1 + nota2)/2)

print()
print("El promedio de las Notas es: ", promedio)

print("Preguntamos si Aprobo o No el Segundo Parcial")
if nota2 >= 7:
    print("Aprobo el Segundo Parcial.")
else:
    print("Desaprobo el Segundo Parcial.")

print("Preguntamos si Mejoro o Bajo su Desempeño")

if nota2 > nota1:
    estado = "Mejoró su Desepeño."
else:
    if nota1 == nota2:
        estado = "Mantuvo la Nota."
    else:
        estado = "Bajo su Desempeño."

print(f'Progreso del 1er al 2do Parcial: {estado}')

'''
Match = Switch

match valor:
    case primero:
        print()
    case segundo:
        print()
    case tercero:
        print()

'''


if promedio >= 7:
    print("Promociona la Materia.")
elif promedio >= 4:
    print("Rinde Final.")
else:
    print("Recursa.")
