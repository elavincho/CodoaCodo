# programa_ppal.py
import verificaciones_numericas
import entrada_teclado
import aritmetica
'''
    Tarea: permite ingresar números
    enteros hasta que se ingresa el valor 0.
    Ademas informa cantidad de números pares
    ingresados y cantidad de números de dos cifras se
    ingresaron.
'''
cant_pares = 0
cant_nros_dos_dig = 0
n = entrada_teclado.ingreso_entero()
while n != 0:
    if verificaciones_numericas.es_par(n):
        cant_pares = cant_pares + 1
    if aritmetica.cant_digitos(n) == 2:
        cant_nros_dos_dig = cant_nros_dos_dig + 1
    n = entrada_teclado.ingreso_entero()

print('Cantidad de pares : ', cant_pares)
print('Cantidad de numeros de dos dígitos : ', cant_nros_dos_dig)
