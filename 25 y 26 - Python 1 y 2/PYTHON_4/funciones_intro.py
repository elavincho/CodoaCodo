# sintaxis básica para definir (declarar) una función en Python

def imprimir_mensaje():
    print("Hola soy una función")

#Cuerpo principal
imprimir_mensaje()

# --------------------------------------
def imprimir_mensaje_cinco_veces():
    for i in range(5):
        print("Este es el mensaje " + str(i))

#Cuerpo principal
imprimir_mensaje_cinco_veces()