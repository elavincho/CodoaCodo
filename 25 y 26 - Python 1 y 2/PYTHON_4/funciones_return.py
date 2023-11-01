# Funciones que devuelven valores (return)
'''
def restar(num1,num2): # recibe 2 parámetros
    resta= num1-num2
    return resta # La fx retorna (devuelve) un valor
# Programa Principal
resultado= restar(10,3)
print("El 1er resultado de la resta es:", resultado) #imprimo el valor de la variable (resultado)
print("El 2do resultado de la resta es:", restar(4,9)) #imprimo lo que retorna la función restar(x,y)

# ---------------------------------------------------------------
# Ejemplo: return que no devuelve ningún valor
def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)
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

# ---------------------------------------------------------------
# Ejemplo: Devolver más de un valor con return
def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3
#Programa principal
cuad, cubo = cuadrado_y_cubo(8)
print(cuad, cubo)
'''
# Devolvemos los diferentes resultados/valores en una lista
def tabla_del(numero):
    resultados = [] #creamos la lista
    for i in range(11):
        resultados.append(numero * i)
    return resultados
#Programa principal
res = tabla_del(3)
print(res)
