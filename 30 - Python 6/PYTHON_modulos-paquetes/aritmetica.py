# aritmetica.py
def cant_digitos(n):
    ''' Tarea: calcula cantidad de dígitos de un número '''
    cant = 0
    while n > 0:
        cant = cant + 1
        n = n // 10
    return cant

def suma_digitos(n):
    ''' Tarea: calcula suma de los dígitos de un número '''
    suma = 0
    while n > 0:
        suma = suma + n % 10
    n = n // 10
    return suma