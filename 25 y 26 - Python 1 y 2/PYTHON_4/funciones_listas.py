# Funciones que reciben listas
'''
def sumar_lista(lista): #pre: recibe una lista.
    suma= 0 # variable que almacenará la sumatoria
    lista[0]= 100 #al primer valor le asigna el número 100
    for elem in lista:
        suma+=elem #acumulador de elementos
    return suma #devuelve la sumatoria de los elementos de la lista

#llamada a la función (programa principal)
numeros= [1,2,10,-5] #Le damos valores a la lista
print("La suma es: " + str(sumar_lista(numeros)))
print(numeros)

# --------------------------------------------------------------
# Funciones que devuelven mas de un valor

def calcular_suma_prom(lista):
    suma= sumar_lista(lista) # Llamando a una fx dentro de otra fx
    prom= suma/len(lista) #Calculo el promedio como la suma dividido 
                          #la cantidad de elementos de la lista
    return suma, prom # La fx retona 2 (dos) valores
                      # con el return, salimos de la fx

# Llamado a una fx que retorna 2 valores (programa principal)
result1, result2 = calcular_suma_prom(numeros) # En cada variable guardamos
                                               # lo que retorne la función
print("La sumatoria es:", result1, "y el promedio es:", result2) # La sumatoria es: 107 y el promedio es: 26.75
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
numeros= crear_lista(N)
mostrar_lista(numeros)
