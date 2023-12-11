# Módulo collections: colecciones de datos
from collections import Counter
numeros = [1,2,3,4,1,2,3,1,2,1]

print(Counter(numeros)) #Counter({1: 4, 2: 3, 3: 2, 4: 1})
print(Counter("Codo a codo")) #Counter({'a': 3, 'p': 1, 'l': 1, 'b': 1, 'r': 1})
print()

coches = "ferrari bmw bmw ferrari bmw fiat mercedes mercedes"
lista_coches = coches.split()
print(lista_coches)
print(Counter(lista_coches)) #Counter({'bmw': 3, 'ferrari': 2, 'mercedes': 1})
print()

campeones_mundiales = "Uruguay Italia Italia Uruguay Alemania Brasil Brasil Inglaterra Brasil Alemania Argentina Italia Argentina Alemania Brasil Francia Brasil Italia España Alemania Francia"
cm = Counter(campeones_mundiales.split())
print(cm.most_common())  #Ordenado por número de repeticiones (campeonatos)
print()
print(cm.most_common(1)) #País más repetido (con más campeonatos)
print()
print(cm.most_common(3)) #Los 3 países con más campeonatos 
print()




