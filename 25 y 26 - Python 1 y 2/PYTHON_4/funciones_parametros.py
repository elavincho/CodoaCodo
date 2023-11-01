# Parámetros de una función
def imprimir_mensaje_N_veces(N): #Tiene 1 parámetro
    for i in range(N):
        print("Este es el mensaje " + str(i))

# Programa principal
imprimir_mensaje_N_veces(3) #Ejemplo sin datos ingresados por el usuario

veces= int(input("Ingrese la cantidad de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces) #Ejemplo con datos ingresados por el usuario

# ----------------------------------------
# Con dos parámetros
def mensaje_personalizado_N_veces(N, mje): #Tiene 2 parámetros
    for i in range(N):
        print(mje)

# Programa principal
# mensaje_personalizado_N_veces(4, "Juan Pablo")

# Variante: función con 2 datos de entrada que recibe como parámetros proporcionados por el usuario. Usamos la misma función pero le pasamos valores nosotros.
cant = int(input("¿Cuántas veces se repetirá el valor? "))
mensaje = input("¿Cuál es el mensaje? ")
mensaje_personalizado_N_veces(cant, mensaje)

# Variante validando el código:
cant = int(input("¿Cuántas veces se repetirá el valor? "))
while cant<=0: #Validamos que el número sea positivo
    print("Dato no válido!")
    cant = int(input("¿Cuántas veces se repetirá el valor? "))
mensaje = input("¿Cuál es el mensaje? ")
mensaje_personalizado_N_veces(cant, mensaje)

# ---------------------------
# Ejemplo utilizando f-string
def multiplicar_por_5(numero):
    print(f'{numero}*5 = {numero * 5}')

print("Comienzo del programa: ")
multiplicar_por_5(7)
print("Siguiente instrucción")
multiplicar_por_5(113)
print("Fin del programa")

# ------------------------------------------------------
# Parámetros opcionales y por defecto
def saludo(nombre, mensaje="encantado de saludarte"):
    print("Hola {}, {}".format(nombre, mensaje))
saludo("Juan Pablo")

# Parámetros opcionales (otro ejemplo)
def fn_raiz(num, raiz=2):#Si no recibe un segundo parámetro calcula la raiz cuadrada (2)
    return num**(1/raiz)
# Prog Ppal
print(fn_raiz(4))
print(fn_raiz(8))
print(fn_raiz(125,3)) #Acá tiene dos parámetros, el número y la raíz, que no necesariamente tiene que estar y si no está tomo por defecto el 2.

# Parámetros posicionales y parámetros con nombre
saludo(mensaje="¿Cómo estás?", nombre="Juan Pablo")
saludo(nombre="Juan Pablo", mensaje="¿Cómo estás?")
saludo("Juan Pablo", mensaje="¿Cómo estás?")