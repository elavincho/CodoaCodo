# Estructuras Iterativas/Repetitivas
# Ciclos Exactos: yo sé la cantidad exacta de repeticiones (while/for).
# Ciclos Condicionales: no sé la cantidad de repeticiones (while).

# Ciclos Exactos
    # While
'''
Realizar un programa que imprima en pantalla los números del 1 al 100.
'''

i= 1            # Inicialización del contador
while i<=10:    # Cuando llegue a 10 quiero que finalice, es una condición (que en algún momento tiene que finalizar)
    print(i)    # Imprimo el contador, con print(i, end='-') se imprimen uno al lado del otro
    i= i+1      # Le sumo 1
print("Fin del programa")

i= 1 #Debemos darle un valor inicial
N= int(input("Ingrese valor máximo del contador: ")) # Sigue siendo exacto porque al momento de ejecutar el While ya conozco el dato
while i<=N:     # Puede pasar que no entre en la condición porque sea falsa de entrada
    print(i)    # El orden es importante (si lo cambiamos tendremos un comportamiento diferente)                 
    i= i+1      # Importante: no debemos olvidar la instrucción que cambia la condición
print("Fin del programa")


    # For
    #Range va a generar una serie de valores entre un valor inicial, un valor final y el incremento entre valor y valor
    #Esta es una sintaxis para Python, que dista bastante de JS o JAVA
    #Tenemos un valor inicial, un fin y un salto/incremento
    #El valor final en el range no es inclusivo, si queremos hacer desde el 1 al 10 debemos colocar 11 como fin (10+1)

for cont in range(1,10,1): #inicio, fin, salto/inc
    print(cont) #cont es de ámbito local, existe dentro del for

#Otro ejemplo con valores ingresados por el usuario
N= int(input("Ingrese valor máximo del contador: "))

for cont in range(1,N+1,1): #inicio, fin, salto/inc
    print(cont) 

#Otra variante del For: sin incremento, que por defecto es 1
for cont in range(1,N+1): #inicio, fin
    print(cont) 

#Otra variante del For: sacarle el valor inicial: arranca con el 0 como valor inicial 
for cont in range(N+1): #fin
    print(cont) 

# Ciclos Condicionales
'''
Realizar un programa que calcule la sumatoria de números enteros ingresados
por teclado. Finaliza el programa ingresando 0.
'''

suma= 0 # Inicializo mi acumulador (sumatoria)
num= int(input("Ingrese un número: "))
while num!=0:   #Cortamos la condiciòn cuando el nùmero sea distinto de 0
                #Si es 0 no entra en el buble o deja de repetirse
    suma+= num # suma= suma+num
    num= int(input("Ingrese un número: "))  #Volvemos a pedir el número para evitar caer en un ciclo infinito
                                            #No debemos olvidar la instrucción que cambia la condición
print("La sumatoria de los números ingresados es:", suma) #Mostramos el resultado