import random

print("----------Aleatoriedad----------")
#Aleatoriedad
# Flotante aleatorio >= 0 y < 1.0
print("Random:", random.random())      

# Flotante aleatorio >= 1 y <10.0       
print("Uniform", random.uniform(1,10))

# Entero aleatorio de 0 a 9, 10 excluído
print("Randrange (1 parámetro):", random.randrange(10))

# Entero aleatorio de 30 a 100
print("Randrange (2 parámetros):", random.randrange(30,101))

# Entero aleatorio de 0 a 100 cada 2 números, múltiplos de 2
print("Randrange (3 parámetros):", random.randrange(0,101,2))

# Entero aleatorio de 0 a 100 cada 5 números, múltiplos de 5
print("Randrange (3 parámetros):", random.randrange(0,101,5))

#Muestras
print("\n-------------Muestras------------")
# Letra aleatoria
print("Muestra:",random.choice('Hola mundo'))

# Elemento aleatorio
print("Choice:",random.choice([1,2,3,4,5]))

# Dos elementos aleatorios
print("Sample:",random.sample([1,2,3,4,5], 2))

#Mezclas
print("\n-------------Mezclas-------------")

# Barajar una lista, queda guardado
lista = [1,2,3,4,5]
print(lista)
random.shuffle(lista)
print("Shuffle:",lista)