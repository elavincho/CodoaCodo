# Instrucción print
print("Hola a todos!") # Incluye salto de línea
print()
print("Estamos aprendiendo Python ", end='') #end='' hace que sea continuo y no pegue el salto de línea
print("en la comisión 12345") # Continúa en la línea anterior
print()
print(12+5) # imprimimos una suma
print()

cadena= "Pepe Argento"
print("Hola",cadena) #, agrega espacio intermedio
print("Hola"+cadena) #+ no agrega espacio intermedio
edad= 35
print("Hola",cadena, "mi edad es", edad) # Concatenamos
#print("Hola",cadena, "mi edad es"+ edad) #Error, no podemos concatenar cadenas con enteros
print("Hola",cadena, "mi edad es"+ str(edad)) #Parseamos entero a string

# print(valor1, valor2, valor3 , .... , valorN)
print(34,45, -7, 1090,"Juan", True)
print()

# Separador de datos
print(11,22,33, sep=' * ') #es un asterisco la sepación
print(11,22,33, sep='\t') #es una tabulacion
print(11,22,33, sep='\n') #es un salto de línea
print(11,22,33, sep='\n\n') #es un doble salto de línea
print()

# Terminador
print(11,22,33, end=' / ') #termina con una línea en vez de con 1 salto
print('otra línea')
print('nueva línea')