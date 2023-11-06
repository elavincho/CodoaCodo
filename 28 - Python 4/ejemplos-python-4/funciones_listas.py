'''
# Funciones que reciben listas
def sumar_lista(lista): #pre: recibe una lista.
    suma = 0 # variable que almacenará la sumatoria
    cant = 0
    for elem in lista:
        suma += elem #acumulador de elementos
        cant += 1
    prom = suma/cant
    return suma, cant, prom #devuelve la sumatoria, la cantidad y el promedio de los elementos de la lista

#llamada a la función (programa principal)
numeros= [1,2,10,-5] #Le damos valores a la lista
suma, cantidad, promedio = sumar_lista(numeros)

print(f'Lista: {numeros}\nSuma: {suma}\nCantidad: {cantidad}\nPromedio: {promedio}')

'''


# ---------------------------------------------------------
# Ejemplo de carga de listas con valores positivos: validación y muestra

def ingresar_positivo():
    cant= int(input("Ingrese un número: "))
    while cant<=0:
        print("Dato no válido!")
        cant= int(input("Ingrese un número: "))
    return cant

def crear_lista(N):
    lista= []
    for i in range(N):
        valor= ingresar_positivo()
        lista.append(valor)
    return lista

def mostrar_lista(lista):
    for valor in lista:
        print(valor, end=" ")
    print()

# Prog Ppal
N=int(input("¿Cuántos valores tendrá la lista?: "))
numeros = crear_lista(N)
mostrar_lista(numeros)

