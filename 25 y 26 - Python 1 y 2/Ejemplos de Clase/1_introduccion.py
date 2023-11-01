print("Hola Comisión 12345?") # Comentario en línea
'''Comentario en 
bloque'''
"""Otro comentario
 en bloque"""

#Tipos de datos
texto = "Estamos aprendiendo Python" #string / cadena
print(texto)
print(type(texto))

valor_entero = 4 #número, detecta el tipo de dato en función del contenido (tipado dinámico)
print(valor_entero + 9)
print(type(valor_entero))

valor_decimal = 4.9
print(valor_decimal + 8)
print(type(valor_decimal))

#Tipado dimámico
valor_entero = "Codo a Codo"
print(valor_entero) # Tipado dinámico (Python lo permite)
# print(valor_entero + 3) # Error por ser fuertemente tipado (no puedo mezclar tipos de datos): 
                         # No se puede usar una variable en un contexto fuera de su tipo.
                         # Si se quisiera, habría que hacer una conversión de tipos.
print(valor_entero + "3") #No da error

valor_logico = True #Booleano
print(valor_logico)
print(type(valor_logico))