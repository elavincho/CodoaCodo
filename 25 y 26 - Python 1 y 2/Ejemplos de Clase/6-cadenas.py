# Cadenas de caracteres
dia="Martes"
mes='Noviembre'
print(dia+mes)
print(dia,mes)

apellido="Martínez"
print(apellido[0]) #Toma la cadena como un vector
print(len(apellido)) #Devuelve el largo de la cadena
print(apellido[7]) #Devuelve el último valor, pero como nose cuantos datos se pueden ingresar, lo correcto es tomar el len y restarle 1
print(apellido[len(apellido)-1]) #Es -1 porque arranca de 0.
print(apellido[-1]) #Pq el negativo siempre va al último caracter


#Programa para obtener el primer caracter, el último y el largo de la cadena
nombre = input("Ingrese su nombre: ")
primer_caracter = nombre[0]
largo_cadena = len(nombre)
ultimo_caracter= nombre[largo_cadena-1]
ultimo_caracter_2 = nombre[-1]


# ultimo_caracter= nombre[-1]
print("--------- INFORME ---------")
print("Primer caracter:", primer_caracter)
print("Último caracter v1:", ultimo_caracter)
print("Último caracter v2:", ultimo_caracter_2)
print("Largo de la cadena:", largo_cadena)


#Las cadenas son objetos, por lo tanto, tienen métodos
nombre_completo="carlos Martínez estrada"
print(nombre_completo.lower()) #minúsculas
print(nombre_completo.upper()) #mayúsculas
print(nombre_completo.capitalize()) #primer letra de la cadena
print(nombre_completo.title()) #primer letra de cada palabra