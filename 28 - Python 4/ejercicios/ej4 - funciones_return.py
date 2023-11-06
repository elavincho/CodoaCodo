# Funciones que retornan valores

def aumentar_cuota(cuota, aumento):
    cuota_aumentada = cuota + cuota * aumento/100
    return cuota_aumentada

def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

def calcular_cuotas(importe):
    tres_cuotas = round(importe / 3, 2)
    seis_cuotas = round(importe * 1.25 / 6, 2)
    nueve_cuotas = round(importe * 1.50 / 9, 2)
    return tres_cuotas, seis_cuotas, nueve_cuotas

def cargar_materias(cantidad):
    materias = []
    for i in range(cantidad):
        materia = input("Ingrese la materia: ")
        materias.append(materia)
    return materias

#Programa principal
cta = int(input("Ingrese el valor de la cuota: "))
aum = int(input("Ingrese el porcentaje de aumento (número entero): "))
cta_aum = aumentar_cuota(cta, aum)
print(f'Cuota \t$ {cta} \nAum \t{aum}%\nTotal \t$ {cta_aum}')




edad = int(input("Ingrese la edad del estudiante: "))
while es_mayor(edad) != True:
    edad = int(input("Debe ser mayor o igual a 18. Ingrese la edad del estudiante: "))
print(f'Edad: {edad}. Es mayor? {es_mayor(edad)}')






imp = int(input("Ingrese el costo del curso: "))
tres, seis, nueve = calcular_cuotas(imp)
print(f'Costo del curso $ {imp}\n - Tres cuotas de $ {tres}\n - Seis cuotas de $ {seis}\n - Nueve cuotas de $ {nueve}')





lista_materias = cargar_materias(4)
print("Listado de materias:")
for i in range(len(lista_materias)):
    print(f'{i+1}- {lista_materias[i]}')