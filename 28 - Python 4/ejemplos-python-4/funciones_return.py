# FUNCIONES QUE DEVUELVEN VALORES (return)

def restar(num1,num2): # recibe 2 parámetros
    resta= num1-num2
    return resta # La fx retorna (devuelve) un valor

# Programa Principal
resultado = restar(10,3)
print("El resultado es:", resultado) #imprimo el valor de la variable (resultado)
print("El resultado es:", restar(4,9)) #imprimo lo que retorna la función restar(x,y)


# ---------------------------------------------------------------
# Ejemplo: return que no devuelve ningún valor
# Esta función buscar averiguar el cuadrado del número sólo si es par
def cuadrado_de_par(numero):
    if numero % 2 == 0:
        print(numero ** 2)
    else:
        return
cuadrado_de_par(8) #64
cuadrado_de_par(3) #nada, porque no es par


# ---------------------------------------------------------------
# Ejemplo: return que devuelve un valor u otro (con if)
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(2)) #True
print(es_par(5)) #False
for i in range(1,11): #Uso de la función dentro de un ciclo: obtenemos los pares en cierto rango
    if es_par(i) == True:
        print(i)

# ---------------------------------------------------------------
# Ejemplo: Devolver más de un valor con return
def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3

#Programa principal
cuad, cubo = cuadrado_y_cubo(8) #Desempaquetado
print(f'Cuadrado: {cuad}\nCubo: {cubo}')

def operaciones(a,b):
    if b != 0:
        return a+b, a-b, a*b, a/b
    else:
        return a+b, a-b, a*b, "Error, b es 0"

#Programa principal
suma, resta, multiplicacion, division = operaciones(10,5) #Desempaquetamos
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


# Devolvemos los diferentes resultados/valores en una lista
def tabla_del(numero):
    resultados = [] #creamos la lista
    for i in range(11):
        resultados.append(numero * i)
    return resultados

#Programa principal
res = tabla_del(3)
print(res)