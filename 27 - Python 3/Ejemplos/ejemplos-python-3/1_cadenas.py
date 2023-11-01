print("****** CADENAS DE CARACTERES ******")

#Escritura y concatenación

cadena1 = "Aprendiendo cadenas de caracteres"
cadena2 = "en Codo a Codo"
print(cadena1)
print(cadena2)
print(cadena1 + cadena2 + " hoy miércoles.")
print(cadena1, cadena2, "hoy miércoles.")
print()

# Combinar comillas simples y dobles
print("Hoy hizo '27 grados' con mucho sol")
print('Hoy hizo "27 grados" con mucho sol')
print()


#Concatenar números y cadenas
edad = 25
altura = 1.78
datos = "La edad es " + str(edad) + " y la altura es " + str(altura)
print(datos)
print()

#Replicación de cadenas
risa = 'ja'
carcajada = risa*5
print(risa)
print(carcajada)
print("-"*10)


#Cadenas multilínea
cadena = """Cadenas
 en más
 de una
 línea
"""
print(cadena)

cadena2 = '''
esto 
es 
un 
comentario
'''
print(cadena2)
print()


#Comparación de cadenas (ASCII y case sensitive)
cad1 = "@" #ALT + 64
cad2 = "^" #ALT + 94
cad3 = "@" #ALT + 64
print(cad1 > cad2)
print(cad1 < cad2)
print(cad1 == cad3)
print()

ciudad = "Córdoba"
if ciudad == "cordoba":
    print("El envío llega mañana.")
else:
    print("El envío llega el lunes.")


#Largo de cadenas y subíndices
nombre = "Pepe Argento"
print(len(nombre))
print(nombre[0])
print(nombre[-1])
print(nombre[len(nombre)-1])


#Métodos upper / lower / capitalize / title
cad = "Estamos aprendiendo Python"
print(cad.upper())
print(cad.lower())
print(cad.capitalize())
print(cad.title())


#Rebanadas (slicing)
# [:] Todos los elementos.
cadena = "Estamos aprendiendo Python"
print(cadena[:])

# [start:] Todos los elementos desde el índice establecido(start).
print(cadena[12:])

# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
print(cadena[:3])

# [start:end] Todos los elementos de un rango de índices.
print(cadena[1:11])

# [start:end:step] Todos los elementos de un rango de índices con saltos.
print(cadena[6:11:2])

# [::step] Todos los elementos con saltos.
print(cadena[::3])

# [::step] Todos los elementos con saltos (negativo).
print(cadena[::-1])


#Operadores de pertenencia: in / not in
cad = "Aprendiendo Python"
print("A" in cad)
print("z" in cad)
print("prendiendo" in cad)
print("D" not in cad)
print("o" not in cad)


#Iterando cadenas
#For
cad = "Python"
for i in cad:
    #print(i)
    print(i, end="") #uno al lado del otro

print()


#While
cad = "Python"
i = 0
while i < len(cad):
    print(cad[i])
    i += 1


#Uso de min y max
cadena = "Python"
print(max(cadena))
print(min(cadena))
