# FUNCIONES CON PARÁMETROS
# Parámetros: Al definir la función
# Argumentos: Al llamarla

# Funciones con un parámetro
def imprimir_mensaje_N_veces(N): #Tiene 1 parámetro
    for i in range(N):
        print("Mensaje " + str(i))

# Programa principal
imprimir_mensaje_N_veces(3) #Ejemplo sin datos ingresados por el usuario

veces= int(input("Ingrese la cantidad de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces) #Ejemplo con datos ingresados por el usuario

# --------------------------------------------------------------------------------
# Funciones con dos parámetros
def mensaje_personalizado_N_veces(N, mje): #Tiene 2 parámetros
    for i in range(N):
        print(mje)

# Programa principal
mensaje_personalizado_N_veces(4, "Juan Pablo")


# Variante: función con 2 datos de entrada que recibe como parámetros proporcionados por el usuario. Usamos la misma función pero le pasamos valores nosotros.
cant = int(input("¿Cuántas veces se repetirá el valor?: "))
mensaje = input("¿Cuál es el mensaje?: ")
mensaje_personalizado_N_veces(cant, mensaje)

# Variante validando el código:
cant = int(input("¿Cuántas veces se repetirá el valor?: "))
while cant<=0: #Validamos que el número sea positivo
    print("Dato no válido!")
    cant = int(input("¿Cuántas veces se repetirá el valor?: "))
mensaje = input("¿Cuál es el mensaje?: ")
while len(mensaje)==0: #Validamos que se haya escrito un mensaje
    print("Debes escribir un mensaje!")
    mensaje = input("¿Cuál es el mensaje?: ")
mensaje_personalizado_N_veces(cant, mensaje)

# ---------------------------
# Ejemplo utilizando f-string
def multiplicar_por_5(numero):
    print(f'{numero}*5 = {numero * 5}')

# Programa principal
print("Comienzo del programa: ")
multiplicar_por_5(7)
print("Siguiente instrucción")
multiplicar_por_5(113)
print("Fin del programa")
# ------------------------------------------------------
# Parámetros opcionales
def sumar(a=2, b=0):
    return a + b

print(sumar(2,6))
print(sumar(5))
print(sumar())


def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {nombre}, {mensaje}")

# Programa principal
saludo("Juan Pablo")
saludo("Juan Pablo", "¿cómo estás?")


# Parámetros opcionales (otro ejemplo)
def fn_raiz(num, raiz=2):#Si no recibe un segundo parámetro calcula la raiz cuadrada (2)
    return num**(1/raiz)

# Programa principal
print(fn_raiz(4))
print(fn_raiz(125,3)) #Acá tiene dos parámetros, el número y la raíz, que no necesariamente tiene que estar y si no está toma por defecto el 2.

# Parámetros posicionales y parámetros con nombre
def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {nombre}, {mensaje}")

saludo(mensaje="¿Cómo estás?", nombre="Juan Pablo")
saludo(nombre="Ana Marìa", mensaje="Bienvenida!")
saludo("Juan Pablo", mensaje="¿Cómo estás?")
