# Errores

# Error de sintaxis
#print("Hola" 

# Error de nombre
# pint("Hola")

# Error de tipo
#a = 3
#b = "7"
#print(a+b)
#print(a+int(b)) #Solución (suma aritmética)
#print(str(a)+b) #Solución (concatenación)

# ZeroDivisionError (error de división por cero)
#print(12/0)

# Error semántico: Ejemplo pop() con lista vacía
#valores = []
#valores.pop()

# Solución a pop() con lista vacía
# valores = [2]
# if len(valores) > 0:
#     valores.pop()
# print(valores)

# Error semántico: Ejemplo lectura de cadena y operación sin conversión a número
#n = input("Ingrese un número: ")
#m = 4
#print(f'{n}/{m} = {n/m}')

# Solución a lectura de cadena y operación sin conversión a número
#n = int(input("Ingrese un número: "))
#m = 4
#print(f'{n}/{m} = {n/m}')