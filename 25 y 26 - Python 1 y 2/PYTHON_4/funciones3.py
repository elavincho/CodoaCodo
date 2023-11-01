# EJEMPLO: USO DE PARÁMETROS POR DEFECTO
'''Tarea: Por cada empleado de una empresa se leen tres datos: legajo, sueldo básico y
antigüedad en la empresa. Emitir un listado que informe:
    - Importe total de salarios pagados.
    - Porcentaje de empleados que ganan más del 20000.
    - Legajo del empleado que más gana.
    - Sueldo más bajo.
    Nota:
    - El salario de la siguiente manera, al sueldo básico se le debe sumar un 5%
    por año de antigüedad, agregando un 25% adicional si la misma supera los
    10 años.
    - El sueldo de los empledos no supera el millon de pesos.
    - El lote de datos finaliza cuando se ingresa el legajo 0 (cero)
    - Validar los datos de entrada
'''
def ingEntPos(mensaje):
    valor = float(input(mensaje))
    while valor != int(valor) or valor < 0:
        valor = float(input('Error. ' + mensaje))
    return int(valor)

def ingRealPos(mensaje):
    valor = float(input(mensaje))
    while valor < 0:
        valor = float(input('Error. ' + mensaje))
    return valor

def porcentaje(parcial, total):
    return parcial * 100 / total

def sueldoNeto(basico, antiguedad = 0):
    neto = basico + 0.05 * basico * antiguedad
    if antiguedad > 10:
        neto += 0.25 * basico
    return neto

# Programa principal
sueldoTotal, cantEmpl, cantEmplMas20Mil = 0, 0, 0
legMasGana, sueldoMasGana, sueldoMenosGana = 0, 0, 1000000
legajo = ingEntPos('Legajo: ')

while legajo != 0:
    ant = ingEntPos('Antiguedad: ')
    sBasico = ingRealPos('Sueldo: ')
    sueldo = sueldoNeto(sBasico) if ant == 0 else sueldoNeto(sBasico, ant)
    sueldoTotal += sueldo
    cantEmpl += 1
    if sueldoMasGana < sueldo:
        sueldoMasGana = sueldo
        legMasGana = legajo
    if sueldoMenosGana > sueldo:
        sueldoMenosGana = sueldo
    if sueldo > 20000:
        cantEmplMas20Mil += 1
    legajo = ingEntPos('Legajo: ')
print(f'Importe total a pagar: {sueldoTotal:10.2f}')
if cantEmpl != 0:
    print(f'Porcentaje de empleados que ganan más del 20000: {porcentaje(cantEmplMas20Mil, cantEmpl): 10.2f}')
    print(f'Empleado que más gana: {legMasGana}')
    print(f'Sueldo más bajo: {sueldoMenosGana}')