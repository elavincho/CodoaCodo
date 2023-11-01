print("****** DICCIONARIOS ******")

#Creación de diccionarios
vacio = {} 			                # diccionario vacío
dicc_uno = {'Juan': 56}			    # diccionario de un elemento
dicc_dos = {'Juan': 56, 'Ana': 15}  # diccionario de dos elementos
print(vacio)
print(dicc_uno)
print(dicc_dos)
print()

#Acceder a elementos
print(dicc_dos.items()) #Mostramos los pares clave-valor
for clave, valor in dicc_dos.items(): #otra manera de mostrar los pares clave-valor
    print(f'{clave}: {valor}')

print(dicc_dos.keys()) #Mostramos las claves
for i in dicc_dos.keys(): #Mostramos los valores
    print(dicc_dos[i], end=' ')
print()

#Modificar elementos
print("Edad de Juan:",dicc_dos["Juan"]) #Valor que corresponde a la clave "Juan"
dicc_dos["Juan"] = 37
print("Nueva edad de Juan:",dicc_dos["Juan"]) 

#Agregar elementos
dicc_dos["Pablo"] = 12
dicc_dos["Julieta"] = 26
print(dicc_dos)
dicc_dos["Pablo"] = 47 #No agrega un nuevo "Pablo", sino que modifica el existente
print(dicc_dos)
print()

#Otra forma de acceder a elementos y mostrarlos: listas
lista_claves = list(dicc_dos.keys()) # Le pido al dicc sus claves y lo convierto a lista
lista_valores = list(dicc_dos.values())

for i in range(len(lista_claves)):
   print(lista_claves[i],"tiene",lista_valores[i],"años") #Imprimimos valores
'''
'''