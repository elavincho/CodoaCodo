#Función que valida el rango entre 1 y 10 y el corte -1
def ingresar_positivo():
    nota = int(input("Ingrese una nota: "))
    while (nota < 1 or nota > 10) and nota != -1:
        nota= int(input("Dato no válido! Ingrese una nota: "))
    return nota

#Función que crea la lista con las notas validadas
def crear_lista():
    lista = [] #Lista vacía
    nota = ingresar_positivo() #Llama a la f ingresar positivo para validar
    while nota != -1:
        lista.append(nota) #Agrega la nota a la lista
        nota = ingresar_positivo()
    return lista

#Función que va a calcular el promedio recorriendo la lista y sumando las notas
def obtener_datos(lista):
    suma = 0
    cantidad_notas = len(lista)
    for i in range(cantidad_notas):
        suma = suma + lista[i]
    promedio = round(suma / cantidad_notas, 2)
    return promedio, cantidad_notas

# Programa principal
lista_notas = crear_lista()
prom, cant = obtener_datos(lista_notas) #La f devuelve el promedio a prom y la cantidad de notas a cant
print(f'Cantidad de notas: {cant}. Promedio: {prom} ')