# Excepciones: Bloques try - except

# n = float(input("Ingrese un número: "))
# m = 4
# print(f'{n}/{m} = {n/m}')

# PRIMER CASO: try-except

'''
try:
    n = float(input("Ingrese un número: "))
    m = 4
    print(f'{n}/{m} = {n/m}')
except:
    print("Ha ocurrido un error, introduzca un número")

print("Sigue...")

''' 
# SEGUNDO CASO: try-except con While 

'''
while(True):
    try:
        n = float(input("Ingrese un número: "))
        m = 4
        print(f'{n}/{m} = {n/m}')
        break # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduzca un número")
''' 

# TERCER CASO: try-except-else con While 

'''
while(True):
    try:
        n = float(input("Ingrese un número: "))
        m = 4
        print(f'{n}/{m} = {n/m}')
    except:
        print("Ha ocurrido un error, introduzca un número")
    else:
        print(f'Se ha ingresado el valor {n}, todo ok')
        break # Importante romper la iteración si todo ha salido bien

''' 

# CUARTO CASO: try-except-else-finally con While 

'''
while(True):
    try:
        n = float(input("Ingrese un número: "))
        m = 4
        print(f'{n}/{m} = {n/m}')
    except:
        print("Ha ocurrido un error, introduzca un número")
    else:
        print(f'Se ha ingresado el valor {n}, todo ok')
        break # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta, se puede utilizar para un bloque de código que quiero siempre se ejecute.
'''